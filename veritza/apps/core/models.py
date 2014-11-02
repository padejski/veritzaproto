# -*- coding: utf-8 -*-

import dateutil

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import UUIDField

from userena.models import UserenaBaseProfile


# CORE VERITZA MODELS ##################################
class User(AbstractUser):
    uuid = UUIDField()
    subscriptions = models.ManyToManyField("Veritza")

    def subscribe(self, veritza):
        self.subscriptions.add(veritza)

    def unsubscribe(self, veritza):
        self.subscriptions.remove(veritza)


class VeritzaBaseModel(models.Model):
    """
    Base abstract model for the Veritza's core models
    """
    class Meta:
        abstract = True

    uuid = UUIDField()
    created_by = models.ForeignKey('User', null=True)
    # modified_by = models.ForeignKey('User', related_name='modified_veritzas')
    created = models.DateTimeField(_("Created Timestamp"), auto_now_add=True)
    updated = models.DateTimeField(_("Last Modified"), auto_now=True)
    active = models.BooleanField(_("Active"), default=True)

    # def __unicode__(self):
    #     if hasattr(self, 'name'):
    #         return getattr(self, 'name')
    #     if hasattr(self, 'title'):
    #         return getattr(self, 'title')
    #     return repr(self)


class UserProfile(UserenaBaseProfile):
    """
    Needed for django-userena AUTH_PROFILE_MODEL setting
    """
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('User'),
                                related_name='profile')


class Person(VeritzaBaseModel):
    national_id = models.CharField(_("National ID"), max_length=40, null=True, blank=True)
    national_id_type = models.CharField(_("National ID Type"), max_length=40, null=True, blank=True)
    first_name = models.CharField(_("First Name"), max_length=255)
    middle_names = models.CharField(_("Middle Names"), max_length=1024, null=True, blank=True)
    last_name = models.CharField(_("Last Name"), max_length=255)
    birth_date = models.DateTimeField(_("Birth Date"), null=True, blank=True)

    def __unicode__(self):
        return u"%s %s - %s" % (self.first_name, self.last_name, self.national_id)


class Dataset(VeritzaBaseModel):
    name = models.CharField(_("Name"), max_length=255)
    source = models.CharField(_("Source"), max_length=512)
    description = models.TextField(_("Description"), null=True, blank=True)
    notes = models.TextField(_("Notes"), null=True, blank=True)
    tags = models.ManyToManyField("Tag", null=True, blank=True)

    def __unicode__(self):
        return self.name


class Veritza(VeritzaBaseModel):
    name = models.CharField(_("Name"), max_length=255)
    sources = models.ManyToManyField(Dataset)
    description = models.TextField(_("Description"), null=True, blank=True)
    notes = models.TextField(_("Notes"), null=True, blank=True)

    def __unicode__(self):
        return self.name

# public_office,spouse_job,spouse_movables,address,spouse_companies,job,spouse_salary,link,year,
# real_estate,spouse_real_estate,public_office_other,spouse,id,movables,salary,name,official_type,companies,rbr,report_name

# class PublicOfficial(VeritzaBaseModel):
#     """
#     From Public officials
#     """
#     full_name
#     office_title
#     official_type


class PublicOfficialReport(VeritzaBaseModel):
    """
    From Public officials
    """
    system_id = models.CharField(max_length=255)  # , unique=True)
    name = models.CharField(max_length=255, null=True, db_index=True)
    public_office = models.CharField(max_length=255, null=True)
    public_office_other = models.CharField(max_length=255, null=True)
    official_type = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    job = models.CharField(max_length=255, null=True)
    salary = models.CharField(max_length=255, null=True)
    movables = models.CharField(max_length=255, null=True)
    real_estate = models.CharField(max_length=255, null=True)
    companies = models.CharField(max_length=255, null=True)
    report_name = models.CharField(max_length=255, null=True)
    report_type = models.CharField(max_length=255, null=True)
    year = models.CharField(max_length=10, null=True)
    rbr = models.CharField(max_length=10, null=True)
    spouse = models.CharField(max_length=255, null=True)
    spouse_job = models.CharField(max_length=255, null=True)
    spouse_salary = models.CharField(max_length=255, null=True)
    spouse_companies = models.CharField(max_length=255, null=True)
    spouse_movables = models.CharField(max_length=255, null=True)
    spouse_real_estate = models.CharField(max_length=255, null=True)
    link = models.URLField(null=True)

    def __unicode__(self):
        # return u"{0} [{1}] ({2})".format(self.name, self.year, self.public_office)
        return u"{0} [{1}]".format(self.name, self.year)

    def from_dict(self, data, commit=True):
        for key, value in data.iteritems():
            if key == 'id':
                self.system_id = data.get('id', "").strip()
            elif hasattr(self, key):
                value = value or ""
                print(value, value.decode('latin-1'), value.decode('utf-8'))
                setattr(self, key, value.decode('utf-8').strip())

        if commit:
            self.save()
        return self


class Company(VeritzaBaseModel):
    """
    From Company registry
    """
    class Meta:
        verbose_name_plural = "Companies"

    registration_number = models.CharField(max_length=255, null=True, db_index=True)
    identification_number = models.CharField(max_length=255, null=True, db_index=True)
    name = models.CharField(max_length=255, null=True)
    full_name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    mail_address = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=32, null=True)
    registration_date = models.DateField(null=True)
    location = models.CharField(max_length=255, null=True)
    activity = models.CharField(max_length=255, null=True)
    economic_activity = models.CharField(max_length=255, null=True)
    link = models.URLField(null=True)

    def __unicode__(self):
        return u"%s - %s" % (self.registration_number, self.full_name)

    def from_dict(self, data, commit=True):
        self.registration_number = data.get('registarski_broj', "").strip()
        self.identification_number = data.get('maticni_broj', "").strip()
        self.name = data.get(u'naziv_društva', "").strip()
        self.full_name = data.get('full_name', "").strip()
        self.address = data.get('address', "").strip()
        self.mail_address = data.get('mail_address', "").strip()
        self.status = data.get('status', "").strip()
        self.registration_date = dateutil.parser.parse(data.get('registration_date'))
        self.location = data.get('mjesto', "").strip()
        self.activity = data.get('djelatnost', "").strip()
        self.economic_activity = data.get('naziv_privredne_djelatnosti', "").strip()
        self.link = data.get('link', "").strip()

        if commit:
            self.save()
        return self


class CompanyMember(VeritzaBaseModel):
    """
    From Company registry
    """
    company_registration_number = models.CharField(max_length=255, db_index=True)
    title = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    company_share = models.CharField(max_length=30, null=True)
    link = models.URLField(null=True)

    def __unicode__(self):
        return u"{0} {1} [{2} - {3}]".format(self.first_name, self.last_name, self.title, self.company_registration_number)

    def full_name(self):
        return u"{0} {1}".format(self.first_name, self.last_name)


# Public Procurement models ###############################
class BidderCompany(VeritzaBaseModel):
    """
    From Public procurement
    """
    class Meta:
        verbose_name_plural = "Bidder Companies"

    procurement_number = models.CharField(max_length=255, db_index=True)
    identification_number = models.CharField(max_length=255, db_index=True)
    name = models.CharField(max_length=255)
    town = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    postal_address = models.CharField(max_length=255, null=True)
    webpage = models.CharField(max_length=255, null=True)
    contact_point = models.CharField(max_length=255, null=True)

    def __unicode__(self):
        return self.name

    def from_dict(self, data, commit=True):
        self.identification_number = data.get('bidder_id', "").strip()
        self.name = data.get('bidder_name', "").strip()
        self.town = data.get('bidder_town', "").strip()
        self.email = data.get('bidder_email', "").strip()
        self.postal_address = data.get('bidder_postal_address', "").strip()
        self.webpage = data.get('bidder_webpage', "").strip()
        self.contact_point = data.get('bidder_contact_point', "").strip()
        if commit:
            self.save()
        return self


class ContractingAuthority(VeritzaBaseModel):

    class Meta:
        verbose_name_plural = "Contracting Authorities"

    procurement_number = models.CharField(max_length=255)
    identification_number = models.CharField(max_length=40, db_index=True)
    name = models.CharField(max_length=255)
    town = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    webpage = models.URLField(null=True)

    def __unicode__(self):
        return self.name

    def from_dict(self, data, commit=True):
        self.name = data.get('contracting_authority').strip()
        if commit:
            self.save()
        return self


class PublicProcurement(VeritzaBaseModel):
    number = models.CharField(max_length=40, null=True)
    system_id = models.CharField(max_length=40, null=True)
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    record_type = models.CharField(_("Notice type"), max_length=255, null=True)
    creation_date = models.DateTimeField(_("Creation Date"), null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return u"{0}: {1}".format(self.number, self.title)

    def from_dict(self, data, commit=True):
        self.number = data.get('identification_number', "").strip()
        self.title = data.get('title', "").strip()
        self.description = data.get('description', "").strip()
        self.record_type = data.get('notice_type', "").strip()
        self.creation_date = dateutil.parser.parse(data.get('creation_date'))
        self.link = dateutil.parser.parse(data.get('link'))

        if commit:
            self.save()
        return self


class ConflictInterest(models.Model):

    class Meta:
        verbose_name = "Conflict of Interest"
        verbose_name_plural = "Conflicts of Interest"

    official = models.ForeignKey(PublicOfficialReport)
    company = models.ForeignKey(Company)
    public_procurement = models.ForeignKey(PublicProcurement)

    def __unicode__(self):
        return u"{0} - {1} [{2}] - {3}".format(self.official.name, self.company.full_name, self.official_title(), self.public_procurement.title)

    def official_title(self):
        return u"{0} [{1}]".format(self.official.public_office, self.official.official_type)

    @classmethod
    def refresh(cls, start=0, end=100000):
        bidders_ids = BidderCompany.objects.all().values_list('identification_number', flat=True)
        companies_ids = Company.objects.filter(identification_number__in=bidders_ids)\
                               .values_list('registration_number', flat=True)
        members_names = [m.full_name() for m in CompanyMember.objects.filter(company_registration_number__in=companies_ids)]
        officials = PublicOfficialReport.objects.filter(name__in=members_names)

        from django.db import connection
        cursor = connection.cursor()

        query_string = """
            SELECT c.id as company, o.id as official, p.id as public_procurement
            FROM core_company c
            JOIN core_biddercompany b
                ON c.identification_number = b.identification_number
            JOIN core_publicprocurement p
                ON b.procurement_number = p.number
            JOIN core_companymember m
                ON m.company_registration_number = c.registration_number
            JOIN core_publicofficialreport o
                ON CONCAT(m.first_name, ' ', m.last_name) = o.name
            WHERE m.id > %s and m.id < %s;
        """
        query_args = [start, end]

        cursor.execute(query_string, query_args)

        conflit_interests = []
        for row in cursor.fetchall():
            ci = cls()
            ci.company_id = row[0]
            ci.official_id = row[1]
            ci.public_procurement_id = row[2]
            conflit_interests.append(ci)
        # print(conflit_interests)
        cls.objects.bulk_create(conflit_interests)
        return len(conflit_interests)

# ADDITIONAL MODELS ##################################


class UserSettings(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)


class Alert(models.Model):
    user = models.ForeignKey("User")
    veritza = models.ForeignKey("Veritza", null=True, blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
