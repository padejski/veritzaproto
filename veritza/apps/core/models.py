# -*- coding: utf-8 -*-

import dateutil
from django.db import models, connection
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import UUIDField

from userena.models import UserenaBaseProfile


# CORE VERITZA MODELS ##################################
class User(AbstractUser):

    class Meta:
        verbose_name_plural = "Users"

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
    class Meta:
        verbose_name_plural = "User profiles"

    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('User'),
                                related_name='profile')


class Person(VeritzaBaseModel):
    class Meta:
        verbose_name_plural = "Persons"

    national_id = models.CharField(_("National ID"), max_length=40, null=True, blank=True)
    national_id_type = models.CharField(_("National ID Type"), max_length=40, null=True, blank=True)
    first_name = models.CharField(_("First Name"), max_length=255)
    middle_names = models.CharField(_("Middle Names"), max_length=1024, null=True, blank=True)
    last_name = models.CharField(_("Last Name"), max_length=255)
    birth_date = models.DateTimeField(_("Birth Date"), null=True, blank=True)

    def __unicode__(self):
        return u"%s %s - %s" % (self.first_name, self.last_name, self.national_id)


class Dataset(VeritzaBaseModel):
    class Meta:
        verbose_name_plural = "Datasets"

    name = models.CharField(_("Name"), max_length=255)
    source = models.CharField(_("Source"), max_length=512)
    description = models.TextField(_("Description"), null=True, blank=True)
    notes = models.TextField(_("Notes"), null=True, blank=True)
    tags = models.ManyToManyField("Tag", null=True, blank=True)

    def __unicode__(self):
        return self.name


class Veritza(VeritzaBaseModel):
    class Meta:
        verbose_name_plural = "Veritzas"

    name = models.CharField(_("Name"), max_length=255)
    sources = models.ManyToManyField(Dataset)
    description = models.TextField(_("Description"), null=True, blank=True)
    notes = models.TextField(_("Notes"), null=True, blank=True)

    def __unicode__(self):
        return self.name


class PublicOfficial(VeritzaBaseModel):
    """
    From Public officials
    """
    class Meta:
        verbose_name_plural = "Public officials"

    system_id = models.CharField(max_length=255, db_index=True, null=True, unique=True)
    name = models.CharField(max_length=255, null=True, db_index=True)

    def __unicode__(self):
        return u"{0}".format(self.name)


class PublicOfficialReport(VeritzaBaseModel):
    """
    From Public officials
    """
    class Meta:
        verbose_name_plural = "Public official reports"

    official = models.ForeignKey(PublicOfficial, null=True)
    system_id = models.CharField(max_length=255, db_index=True)
    name = models.CharField(max_length=255, null=True, db_index=True)

    report_name = models.CharField(max_length=255, null=True, help_text=u"Naziv izvještaja")
    report_type = models.CharField(max_length=255, null=True, help_text=u"")
    year = models.CharField(max_length=10, null=True, help_text=u"Godina")
    rbr = models.CharField(max_length=10, null=True, help_text=u"Rbr")
    link = models.URLField(null=True, help_text=u"Link")

    public_office = models.CharField(max_length=255, null=True, help_text=u"Javna funkcija")
    public_office_other = models.CharField(max_length=255, null=True, help_text=u"Druga javna funkcija")
    official_type = models.CharField(max_length=255, null=True, help_text=u"Vrsta funkcionera")
    address = models.CharField(max_length=255, null=True, help_text=u"Adresa")

    job = models.CharField(max_length=255, null=True, help_text=u"Stalni radni odnos")
    company_board_member = models.CharField(max_length=1024, null=True, help_text=u"Član organa privrednog društva")
    salary = models.CharField(max_length=255, null=True, help_text=u"Mjesečna nadoknada")
    other_activities = models.CharField(max_length=1024, null=True, help_text=u"Obavljanje drugih djelatnosti")
    other_activities_salary = models.CharField(max_length=1024, null=True, help_text=u"Mjesečna nadoknada")
    real_estate = models.CharField(max_length=1024, null=True, help_text=u"Nepokretna imovina")
    movables = models.CharField(max_length=1024, null=True, help_text=u"Pokretna imovina")
    movables_others = models.CharField(max_length=1024, null=True, help_text=u"Ostala pokretna imovina")
    companies = models.CharField(max_length=1024, null=True, help_text=u"Vlasništvo u privrednim društvima")
    company_salary = models.CharField(max_length=255, null=True, help_text=u"Mjesečna plata")
    annual_income = models.CharField(max_length=255, null=True, help_text=u"Godišnji prihod od poljoprivrede i dr. djelatnosti")
    other_income = models.CharField(max_length=255, null=True, help_text=u"Ostali prihodi")
    credits_debts = models.CharField(max_length=255, null=True, help_text=u"Krediti, dugovi i potraživanja")

    spouse = models.CharField(max_length=255, null=True, help_text=u"Ime bračnog/vanbračnog druga")
    spouse_job = models.CharField(max_length=255, null=True, help_text=u"Stalni radni odnos")
    spouse_other_activities = models.CharField(max_length=1024, null=True, help_text=u"Obavljanje drugih djelatnosti")
    spouse_movables = models.CharField(max_length=255, null=True, help_text=u"Pokretna imovina")
    spouse_movables_others = models.CharField(max_length=1024, null=True, help_text=u"Ostala pokretna imovina")
    spouse_real_estate = models.CharField(max_length=255, null=True, help_text=u"Nepokretna imovina")
    spouse_companies = models.CharField(max_length=255, null=True, help_text=u"Vlasništvo u privrednim društvima")
    spouse_company_salary = models.CharField(max_length=255, null=True, help_text=u"Mjesečna plata")
    spouse_annual_income = models.CharField(max_length=255, null=True, help_text=u"Godišnji prihod od poljoprivrede i dr. djelatnosti")
    spouse_other_income = models.CharField(max_length=255, null=True, help_text=u"Ostali prihodi")
    spouse_credits_debts = models.CharField(max_length=255, null=True, help_text=u"Krediti, dugovi i potraživanja")

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

    @classmethod
    def match_to_officials(cls):
        cursor = connection.cursor()

        query_string = """
            SELECT por.id, po.id
            FROM core_publicofficialreport por
            JOIN core_publicofficial po
                ON por.system_id = po.system_id
        """
        query_args = []

        cursor.execute(query_string, query_args)

        for row in cursor.fetchall():
            por = cls.objects.get(id=row[0])
            por.official_id = row[1]
            por.save()


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
    activity = models.CharField(_("Economic activity"), max_length=255, null=True)
    economic_activity = models.CharField(_("Company type"), max_length=255, null=True)
    link = models.URLField(null=True)

    def __unicode__(self):
        return u"%s [%s]" % (self.full_name, self.registration_number)

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
    class Meta:
        verbose_name_plural = "Company members"

    company = models.ForeignKey('Company', null=True)
    company_registration_number = models.CharField(max_length=255, db_index=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    link = models.URLField(null=True)

    def __unicode__(self):
        return u"{0} {1} [{2}]".format(self.first_name, self.last_name, self.company_registration_number)

    def full_name(self):
        return u"{0} {1}".format(self.first_name, self.last_name)


class CompanyMemberTitle(VeritzaBaseModel):
    """
    From Company registry
    """
    class Meta:
        verbose_name_plural = "Company member titles"

    company_registration_number = models.CharField(max_length=255, db_index=True)
    company_member = models.ForeignKey(CompanyMember, null=True)
    title = models.CharField(max_length=255, null=True)
    company_share = models.CharField(max_length=30, null=True)

    def __unicode__(self):
        return u"{0} {1} - {2}".format(self.company_member.first_name, self.company_member.last_name, self.title)

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

    class Meta:
        verbose_name_plural = "Public procurements"

    number = models.CharField(max_length=40, null=True)
    system_id = models.CharField(max_length=40, null=True)
    title = models.CharField(max_length=255, null=True)
    subject = models.CharField(max_length=255, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    location = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    record_type = models.CharField(_("Notice type"), max_length=255, null=True)
    creation_date = models.DateTimeField(_("Creation Date"), null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return u"{0}: {1}".format(self.number, self.title)

    def from_dict(self, data, commit=True):
        self.number = data.get('identification_number', "").strip()
        self.title = data.get('title', "").strip()
        self.subject = data.get('subject', "").strip()
        self.description = data.get('description', "").strip()
        self.record_type = data.get('notice_type', "").strip()
        self.creation_date = dateutil.parser.parse(data.get('creation_date'))
        self.link = dateutil.parser.parse(data.get('link'))

        if commit:
            self.save()
        return self


class PublicOfficialCompany(models.Model):

    class Meta:
        verbose_name = "Public official's company"
        verbose_name_plural = "Public officials companies"
        # unique_together = ('official', 'company')

    official = models.ForeignKey(PublicOfficial)
    company = models.ForeignKey(Company)

    def __unicode__(self):
        return u"{0} - {1}".format(self.official.name, self.company.full_name)

    @classmethod
    def refresh(cls):

        cursor = connection.cursor()

        query_string = """
            SELECT c.id as company, o.id as official
            FROM core_company c
            JOIN core_companymember m
                ON m.company_registration_number = c.registration_number
            JOIN core_publicofficial o
                ON CONCAT(m.first_name, ' ', m.last_name) = o.name
            WHERE c.registration_number != ""
                AND c.registration_number is not null
                AND o.name != ""
                AND o.name is not null;
        """
        query_args = []

        cursor.execute(query_string, query_args)

        official_companies = []
        rows = cursor.fetchall()
        for row in rows:
            oc = cls()
            oc.company_id = row[0]
            oc.official_id = row[1]
            official_companies.append(oc)
            if len(official_companies) > 50:
                cls.objects.bulk_create(official_companies)
                official_companies = []
        cls.objects.bulk_create(official_companies)


class ConflictInterest(models.Model):

    class Meta:
        verbose_name = "Conflict of Interest"
        verbose_name_plural = "Conflicts of Interest"
        # unique_together = ('official', 'company', 'public_procurement')

    official = models.ForeignKey(PublicOfficial)
    company = models.ForeignKey(Company)
    public_procurement = models.ForeignKey(PublicProcurement)

    def __unicode__(self):
        # return u"{0} - {1} [{2}] - {3}".format(self.official.name, self.company.full_name, self.official_title(), self.public_procurement.title)
        return u"{0} - {1} [{2}]".format(self.official.name, self.company.full_name, self.public_procurement.title)

    def official_title(self):
        return ""
        return u"{0} [{1}]".format(self.official.public_office, self.official.official_type)

    @classmethod
    def refresh(cls, start=0, end=100000):
        # bidders_ids = BidderCompany.objects.all().values_list('identification_number', flat=True)
        # companies_ids = Company.objects.filter(identification_number__in=bidders_ids)\
        #                        .values_list('registration_number', flat=True)
        # members_names = [m.full_name() for m in CompanyMember.objects.filter(company_registration_number__in=companies_ids)]
        # officials = PublicOfficialReport.objects.filter(name__in=members_names)

        cursor = connection.cursor()

        # query_string = """
        #     SELECT c.id as company, o.id as official, p.id as public_procurement
        #     FROM core_company c
        #     JOIN core_biddercompany b
        #         ON c.identification_number = b.identification_number
        #     JOIN core_publicprocurement p
        #         ON b.procurement_number = p.number
        #     JOIN core_companymember m
        #         ON m.company_registration_number = c.registration_number
        #     JOIN core_publicofficial o
        #         ON CONCAT(m.first_name, ' ', m.last_name) = o.name
        #     WHERE b.identification_number != ""
        #         AND b.identification_number is not null
        #         AND b.procurement_number != ""
        #         AND b.procurement_number is not null
        #         AND m.id > %s and m.id < %s;
        # """
        query_string = """
            SELECT c.id as company, poc.official_id as official, p.id as public_procurement
            FROM core_company c
            JOIN core_biddercompany b
                ON c.identification_number = b.identification_number
            JOIN core_publicprocurement p
                ON b.procurement_number = p.number
            JOIN core_publicofficialcompany poc
                ON poc.company_id = c.id
            WHERE b.identification_number != ""
                AND b.identification_number is not null
                AND b.procurement_number != ""
                AND b.procurement_number is not null;
        """
        query_args = []

        cursor.execute(query_string, query_args)

        conflit_interests = []
        for row in cursor.fetchall():
            ci = cls()
            ci.company_id = row[0]
            ci.official_id = row[1]
            ci.public_procurement_id = row[2]
            conflit_interests.append(ci)
        cls.objects.bulk_create(conflit_interests, batch_size=500)
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
