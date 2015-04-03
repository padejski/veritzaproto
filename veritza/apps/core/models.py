# -*- coding: utf-8 -*-

import csv
import logging
import dateutil
from datetime import datetime

from django.conf import settings
from django.db.models import signals, Avg, Min, Max, Sum, Count
from django.db import models, connection
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import UUIDField

from userena.models import UserenaBaseProfile

from veritza.apps.core.storages import DummyStorage

logger = logging.getLogger('debug')


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
    is_ok = models.NullBooleanField()

    # def __unicode__(self):
    #     if hasattr(self, 'name'):
    #         return getattr(self, 'name')
    #     if hasattr(self, 'title'):
    #         return getattr(self, 'title')
    #     return repr(self)

    def get_class(self):
        return self.__class__


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


class ContributorCompanyProcurement(VeritzaBaseModel):
    company = models.ForeignKey('Company')
    procurement = models.ForeignKey('PublicProcurement')
    contribution_record = models.ForeignKey('ElectionsContributions')

    def __unicode__(self):
        return u"{0} [{1}] / {2}".format(
            self.company.name,
            self.company.identification_number,
            self.procurement_number
        )

    @classmethod
    def refresh(cls, delete_old=True, **kwargs):

        if delete_old:
            cls.objects.all().delete()

        cursor = connection.cursor()

        query_string = """
            SELECT c.id as company, p.id as procurement, cn.id as contribution
            # FROM core_company c
            # JOIN core_companymember m
            #     ON m.company_registration_number = c.registration_number
            # JOIN core_familymember f
            #     ON CONCAT(m.first_name, ' ', m.last_name) = f.name
            # WHERE c.registration_number != ''
            #     AND m.company_registration_number is not null
            #     AND m.company_registration_number != ''
            #     AND f.name != ''
            #     AND f.name is not null
            #     AND c.registration_number is not null
            #     AND c.registration_number != '';
        """
        query_args = []

        cursor.execute(query_string, query_args)

        company_contributors_procurements = []
        rows = cursor.fetchall()
        for row in rows:
            ccp = cls()
            ccp.company = row[0]
            ccp.procurement = row[1]
            ccp.contribution = row[2]

            company_contributors_procurements.append(ccp)

            if len(company_contributors_procurements) > 50:
                cls.objects.bulk_create(company_contributors_procurements)
                company_contributors_procurements = []

        cls.objects.bulk_create(company_contributors_procurements)


class ContributorIndividualProcurement(VeritzaBaseModel):
    individual = models.ForeignKey('CompanyMember')
    company = models.ForeignKey('Company')
    procurement = models.ForeignKey('PublicProcurement')
    contribution_record = models.ForeignKey('ElectionsContributions')

    def __unicode__(self):
        return u"{0} [{1}] / {2} - {3} {4}".format(
            self.company.name,
            self.company.identification_number,
            self.procurement_number,
            self.individual.first_name,
            self.individual.last_name
        )

    @classmethod
    def refresh(cls, delete_old=True, **kwargs):

        if delete_old:
            cls.objects.all().delete()

        cursor = connection.cursor()

        query_string = """
            SELECT cm.id as individual, c.id as company, p.id as procurement, cn.id as contribution
            # FROM core_company c
            # JOIN core_companymember m
            #     ON m.company_registration_number = c.registration_number
            # JOIN core_familymember f
            #     ON CONCAT(m.first_name, ' ', m.last_name) = f.name
            # WHERE c.registration_number != ''
            #     AND m.company_registration_number is not null
            #     AND m.company_registration_number != ''
            #     AND f.name != ''
            #     AND f.name is not null
            #     AND c.registration_number is not null
            #     AND c.registration_number != '';
        """
        query_args = []

        cursor.execute(query_string, query_args)

        individuals_contributors_procurements = []
        rows = cursor.fetchall()
        for row in rows:
            cip = cls()
            cip.individual = row[0]
            cip.company = row[1]
            cip.procurement = row[2]
            cip.contribution = row[3]

            individuals_contributors_procurements.append(cip)

            if len(individuals_contributors_procurements) > 50:
                cls.objects.bulk_create(individuals_contributors_procurements)
                individuals_contributors_procurements = []

        cls.objects.bulk_create(individuals_contributors_procurements)


class ElectionsContributions(VeritzaBaseModel):
    """
    From Elections commission database
    """
    class Meta:
        verbose_name_plural = "Elections contributions"

    date = models.DateField(null=True, blank=True)
    election_type = models.CharField(max_length=255, null=True, blank=True)
    election_place = models.CharField(max_length=40, null=True, blank=True)
    political_party = models.CharField(max_length=1024, null=True, blank=True)
    candidate = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    contributor_type = models.CharField(max_length=255, null=True, blank=True)
    contributor_name = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    contributor_address = models.CharField(max_length=255, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    csv_file = models.FileField(storage=DummyStorage(), upload_to=settings.MEDIA_ROOT, null=True, blank=True)

    def __unicode__(self):
        candidate = self.candidate + ', ' if self.candidate else ''
        return u"{0} to {1}{2}: {3}".format(self.contributor_name, candidate, self.political_party, self.amount)

    @classmethod
    def import_from_csv(cls, file, created_by=None):
        records = []
        reader = csv.reader(file.read().splitlines())
        columns = map(lambda c: c.replace('-', '_'), reader.next())
        for values in reader:
            data = dict(zip(columns, [value.decode('latin-1') for value in values]))
            try:
                data['date'] = datetime.strftime(datetime.strptime(data['date'], "%d.%m.%Y."), "%Y-%m-%d")
            except ValueError as exc:
                try:
                    # Try same date format ubt without the dot at the end
                    data['date'] = datetime.strftime(datetime.strptime(data['date'], "%d.%m.%Y"), "%Y-%m-%d")
                except ValueError as exc:
                    logger.exception(exc)
                else:
                    records.append(ElectionsContributions(created_by=created_by, **data))
            else:
                records.append(ElectionsContributions(created_by=created_by, **data))
        cls.objects.bulk_create(records)

    @classmethod
    def stats(cls):
        data = {}
        data = cls.objects.aggregate(Min('amount'), Avg('amount'), Max('amount'))
        data.update(cls.objects.aggregate(Min('date'), Max('date')))
        data['min_amount_contributions'] = cls.objects.select_related().filter(amount__lte=data['amount__min'])
        data['max_amount_contributions'] = cls.objects.select_related().filter(amount__gte=data['amount__max'])

        return data


class ElectionsContributionCompanyMember(VeritzaBaseModel):
    """
    Veritza: Individuals  which have contributed  to political parties on elections
             and which are company members in companies which were awarded public procurements
    """
    company_member = models.ForeignKey('CompanyMember')
    company = models.ForeignKey('Company', null=True, blank=True)
    election_contribution = models.ForeignKey('ElectionsContributions')

    class Meta:
        verbose_name_plural = "Elections Contribution Company Members"

    def __unicode__(self):
        return u"Member ID: {0} (Company: {1}), Contribution: {2}".format(self.company_member_id, self.company_id, self.election_contribution_id)

    @classmethod
    def refresh(cls, delete_old=True, **kwargs):

        if delete_old:
            cls.objects.all().delete()

        cursor = connection.cursor()

        query_string = """
            SELECT
                cm.id as company_member_id,
                c.id as company_id,
                e.id as election_contribution_id
            FROM
                core_electionscontributions e
            JOIN
                core_companymember cm
                ON LOWER(e.contributor_name) = LOWER(CONCAT(cm.first_name, ' ', cm.last_name))
            JOIN
                core_company c
                ON cm.company_id = c.id
            JOIN
                core_procurementcompany p
                ON p.identification_number = c.identification_number
            WHERE
                e.contributor_type = 'individual';
        """
        query_args = []

        cursor.execute(query_string, query_args)

        objects = []
        for row in cursor.fetchall():
            obj = ElectionsContributionCompanyMember()
            obj.company_member_id = row[0]
            obj.company_id = row[1]
            obj.election_contribution_id = row[2]
            objects.append(obj)
        ElectionsContributionCompanyMember.objects.bulk_create(objects)
        return len(objects)


class ElectionsContributionCompany(VeritzaBaseModel):
    """
    Veritza: Companies which have contributed to political parties on elections
             and which were awarded public procurements
    """
    company = models.ForeignKey('Company')
    election_contribution = models.ForeignKey('ElectionsContributions')

    class Meta:
        verbose_name_plural = "Elections Contribution Companies"

    def __unicode__(self):
        return u"Company ID: {0}, Contribution ID: {1}".format(self.company_id, self.election_contribution_id)

    @classmethod
    def refresh(cls, delete_old=True, **kwargs):

        if delete_old:
            cls.objects.all().delete()

        cursor = connection.cursor()

        query_string = """
            SELECT
                c.id as company_id,
                e.id as election_contribution_id
            FROM
                core_electionscontributions e
            JOIN
                core_company c
                ON e.contributor_name = c.name
            JOIN
                core_procurementcompany p
                ON p.identification_number = c.identification_number
            WHERE
                e.contributor_type = 'company';
        """
        query_args = []

        cursor.execute(query_string, query_args)

        objects = []
        for row in cursor.fetchall():
            obj = ElectionsContributionCompany()
            obj.company_id = row[0]
            obj.election_contribution_id = row[1]
            objects.append(obj)
        ElectionsContributionCompany.objects.bulk_create(objects)
        return len(objects)


class PublicOfficial(VeritzaBaseModel):
    """
    From Public officials
    """
    class Meta:
        verbose_name_plural = "Public officials"

    PUBLIC_OFFICIALS_BASE_URL = "http://www.konfliktinteresa.me/funkcioneri/EvidFunPrijave.php?ID="

    system_id = models.CharField(max_length=255, db_index=True, null=True, unique=True)
    name = models.CharField(max_length=255, null=True, db_index=True)

    def __unicode__(self):
        return u"{0}".format(self.name)

    @property
    def link(self):
        return "{0}{1}".format(self.PUBLIC_OFFICIALS_BASE_URL, self.system_id)

    @property
    def companies(self):
        """
        Return QuerySet
        """
        return self.publicofficialcompany_set.all()


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


class FamilyMember(VeritzaBaseModel):

    class Meta:
        verbose_name_plural = "Family members"

    FAMILY_RELATION_CHOICES = {
        '1': 'Spouse',
        '2': 'Daughter',
        '3': 'Son',
    }

    public_official = models.ForeignKey('PublicOfficial')
    name = models.CharField(max_length=255)
    relationship = models.CharField(max_length=40, choices=FAMILY_RELATION_CHOICES.items())

    def __unicode__(self):
        return u"{0} ({1} of {2})".format(self.name, self.FAMILY_RELATION_CHOICES[self.relationship], self.public_official.name)

    @classmethod
    def refresh(cls, delete_old=False, **kwargs):

        if delete_old:
            cls.objects.all().delete()

        # TODO: what if an official divorced and got married again, while in office?
        members = {}
        for report in PublicOfficialReport.objects.filter(spouse__isnull=False).exclude(spouse=''):
            if not members.setdefault(report.official.id, ''):
                members[report.official.id] = cls(public_official=report.official, relationship='1', name=report.spouse)
        cls.objects.bulk_create(members.values())
        return len(members)


    @classmethod
    def stats(cls):
        data = {}
        # data = cls.objects.aggregate(Min('amount'), Avg('amount'), Max('amount'))
        # data.update(cls.objects.aggregate(Min('date'), Max('date')))
        # data['min_amount_contributions'] = cls.objects.select_related().filter(amount__lte=data['amount__min'])
        # data['max_amount_contributions'] = cls.objects.select_related().filter(amount__gte=data['amount__max'])

        return data

class FamilyMemberCompany(VeritzaBaseModel):

    class Meta:
        verbose_name_plural = "Family member companies"

    member = models.ForeignKey('FamilyMember')
    company = models.ForeignKey('Company')

    def __unicode__(self):
        return u"{0}: {1}".format(self.member.name, self.company.full_name)

    @classmethod
    def refresh(cls, delete_old=True, **kwargs):

        if delete_old:
            cls.objects.all().delete()

        cursor = connection.cursor()

        query_string = """
            SELECT c.id as company, f.id as member
            FROM core_company c
            JOIN core_companymember m
                ON m.company_registration_number = c.registration_number
            JOIN core_familymember f
                ON CONCAT(m.first_name, ' ', m.last_name) = f.name
            WHERE c.registration_number != ''
                AND m.company_registration_number is not null
                AND m.company_registration_number != ''
                AND f.name != ''
                AND f.name is not null
                AND c.registration_number is not null
                AND c.registration_number != '';
        """
        query_args = []

        cursor.execute(query_string, query_args)

        members_companies = []
        rows = cursor.fetchall()
        for row in rows:
            fmc = cls()
            fmc.company_id = row[0]
            fmc.member_id = row[1]
            members_companies.append(fmc)
            if len(members_companies) > 50:
                cls.objects.bulk_create(members_companies)
                members_companies = []
        cls.objects.bulk_create(members_companies)


class Company(VeritzaBaseModel):
    """
    From Company registry
    """
    class Meta:
        verbose_name_plural = "Companies"

    registration_number = models.CharField(max_length=255, null=True, db_index=True)
    identification_number = models.CharField(max_length=255, null=True, db_index=True)
    system_id = models.CharField(max_length=40)
    name = models.CharField(max_length=255, null=True)
    full_name = models.CharField(max_length=1024, null=True)
    address = models.CharField(max_length=1024, null=True)
    mail_address = models.CharField(max_length=1024, null=True)
    status = models.CharField(max_length=32, null=True)
    registration_date = models.DateField(null=True)
    location = models.CharField(max_length=255, null=True)
    activity = models.CharField(_("Economic activity"), max_length=1024, null=True)
    economic_activity = models.CharField(_("Company type"), max_length=1024, null=True)
    link = models.URLField(null=True)

    def __unicode__(self):
        return u"%s [%s]" % (self.full_name, self.identification_number)

    def save(self, *args, **kwargs):
        if not self.system_id:
            self.system_id = int(self.link.split('=')[-1])
        super(Company, self).save(*args, **kwargs)

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

    def get_class(self):
        return self.__class__

    @classmethod
    def stats(cls):
        data = {}
        data.update(cls.objects.aggregate(Min('registration_date'), Max('registration_date')))
        return data


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

    class Meta:
        verbose_name_plural = "Bidder companies"

    company = models.ForeignKey('Company')
    procurement = models.ForeignKey('PublicProcurement')

    def __unicode__(self):
        return u"{0} - {1}".format(self.company.full_name, self.procurement.number)

    @classmethod
    def refresh(cls, delete_old=False):

        if delete_old:
            cls.objects.all().delete()

        cursor = connection.cursor()

        query_string = """
            SELECT c.id as company, p.id as procurement
            FROM core_company c
            JOIN core_procurementcompany pc
                ON pc.identification_number = c.identification_number
            JOIN core_publicprocurement p
                ON p.number = pc.procurement_number
                AND p.system_id = pc.procurement_system_id
            WHERE c.identification_number is not null
                AND c.identification_number != ''
                AND pc.identification_number is not null
                AND pc.identification_number != ''
                AND pc.procurement_number is not null
                AND pc.procurement_number != ''
                AND pc.procurement_system_id is not null
                AND pc.procurement_system_id != ''
                AND p.system_id is not null
                AND p.system_id != ''
                AND p.number is not null
                AND p.number != '';
        """

        # query_string = """
        #     SELECT pc.id as company, p.id as procurement
        #     FROM core_procurementcompany pc
        #     JOIN core_publicprocurement p
        #         ON p.number = pc.procurement_number
        #     WHERE  c.identification_number is not null
        #         AND c.identification_number != ''
        #         AND pc.identification_number is not null
        #         AND pc.identification_number != ''
        #         AND p.number is not null
        #         AND p.number != '';
        # """
        query_args = []

        cursor.execute(query_string, query_args)

        bidder_companies = []
        rows = cursor.fetchall()
        for row in rows:
            bc = cls()
            bc.company_id = row[0]
            bc.procurement_id = row[1]
            bidder_companies.append(bc)
            if len(bidder_companies) > 50:
                cls.objects.bulk_create(bidder_companies)
                bidder_companies = []
        cls.objects.bulk_create(bidder_companies)


class ProcurementCompanyRaw(VeritzaBaseModel):
    """
    From Public procurement
    """
    class Meta:
        verbose_name_plural = "Procurement Companies (Raw)"

    procurement_system_id = models.CharField(max_length=40, null=True, help_text="Internal ID in the database where the data is scraped from")
    procurement_number = models.CharField(max_length=255, db_index=True, help_text="Procurement official number (ID). Not certain that it is unique!")
    identification_number = models.CharField(max_length=255, db_index=True, help_text="ID number of the company which was awarded the procurement")
    name = models.CharField(max_length=1024)
    town = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True)
    postal_address = models.CharField(max_length=1024, null=True)
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


class ProcurementCompany(VeritzaBaseModel):
    """
    From Public procurement
    """
    class Meta:
        verbose_name_plural = "Procurement Companies"

    procurement_system_id = models.CharField(max_length=40, null=True, help_text="Internal ID in the database where the data is scraped from")
    procurement_number = models.CharField(max_length=255, db_index=True)
    identification_number = models.CharField(max_length=255, db_index=True)
    name = models.CharField(max_length=1024)
    town = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True)
    postal_address = models.CharField(max_length=1024, null=True)
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

    @classmethod
    def refresh(cls, delete_old=False, **kwargs):

        if delete_old:
            cls.objects.all().delete()

        uniques = ProcurementCompanyRaw.objects.all().distinct('identification_number')
        cls.objects.bulk_create(uniques)
        return len(uniques)


class ContractingAuthority(VeritzaBaseModel):

    class Meta:
        verbose_name_plural = "Contracting Authorities"

    procurement_system_id = models.CharField(max_length=40, null=True, help_text="Internal ID in the database where the data is scraped from")
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
    system_id = models.CharField(max_length=40, null=True, help_text="Internal ID in the database where the data is scraped from")
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

    @classmethod
    def stats(cls):
        data = {}
        data = cls.objects.aggregate(Min('value'), Avg('value'), Max('value'))
        data.update(cls.objects.aggregate(Min('creation_date'), Max('creation_date')))
        data['min_value_procurements'] = cls.objects.select_related().filter(value__lte=data['value__min'])
        data['max_value_procurements'] = cls.objects.select_related().filter(value__gte=data['value__max'])

        return data


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
    def refresh(cls, delete_old=False, **kwargs):

        if delete_old:
            cls.objects.all().delete()

        cursor = connection.cursor()

        query_string = """
            SELECT c.id as company, o.id as official
            FROM core_company c
            JOIN core_companymember m
                ON m.company_registration_number = c.registration_number
            JOIN core_publicofficial o
                ON CONCAT(m.first_name, ' ', m.last_name) = o.name
            WHERE c.registration_number != ''
                AND m.company_registration_number is not null
                AND m.company_registration_number != ''
                AND o.name != ''
                AND o.name is not null
                AND c.registration_number is not null
                AND c.registration_number != '';
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


class ConflictInterestFamilyMember(models.Model):
    class Meta:
        verbose_name = "Conflict of Interest (Family Members)"
        verbose_name_plural = "Conflicts of interest (Family Members)"

    member = models.ForeignKey('FamilyMember')
    company = models.ForeignKey('Company')
    public_procurement = models.ForeignKey('PublicProcurement')

    def __unicode__(self):
        return u"{0} - {1} [{2}]".format(self.member.name, self.company.full_name, self.public_procurement.title)

    @classmethod
    def refresh(cls, delete_old=False, **kwargs):

        if delete_old:
            cls.objects.all().delete()

        cursor = connection.cursor()

        query_string = """
            SELECT fmc.company_id as company, fmc.member_id as member, b.procurement_id as public_procurement
            FROM core_biddercompany b
            JOIN core_familymembercompany fmc
                ON fmc.company_id = b.company_id;
        """
        query_args = []

        cursor.execute(query_string, query_args)

        conflit_interests = []
        for row in cursor.fetchall():
            ci = cls()
            ci.company_id = row[0]
            ci.member_id = row[1]
            ci.public_procurement_id = row[2]
            conflit_interests.append(ci)
        cls.objects.bulk_create(conflit_interests, batch_size=500)
        return len(conflit_interests)


class ConflictInterest(models.Model):

    class Meta:
        verbose_name = "Conflict of Interest"
        verbose_name_plural = "Conflicts of interest"
        # unique_together = ('official', 'company', 'public_procurement')

    official = models.ForeignKey(PublicOfficial)
    company = models.ForeignKey(Company)
    public_procurement = models.ForeignKey(PublicProcurement)

    def __unicode__(self):
        return u"{0} - {1} [{2}]".format(self.official.name, self.company.full_name, self.public_procurement.title)

    def official_title(self):
        return ""
        return u"{0} [{1}]".format(self.official.public_office, self.official.official_type)

    @classmethod
    def refresh(cls, delete_old=False, start=0, end=100000, **kwargs):

        if delete_old:
            cls.objects.all().delete()

        cursor = connection.cursor()

        query_string = """
            SELECT poc.company_id as company, poc.official_id as official, b.procurement_id as public_procurement
            FROM core_biddercompany b
            JOIN core_publicofficialcompany poc
                ON poc.company_id = b.company_id;
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


# SIGNALS CONNECTING ############################################
def parse_csv(sender, instance=None, created=None, **kwargs):
    if instance.csv_file:
        sender.import_from_csv(instance.csv_file, created_by=instance.created_by)

signals.pre_save.connect(parse_csv, sender=ElectionsContributions)


def refresh_all_veritzas(delete_old=False):
    ProcurementCompany.refresh(delete_old=delete_old)
    BidderCompany.refresh(delete_old=delete_old)
    PublicOfficialCompany.refresh(delete_old=delete_old)
    ConflictInterest.refresh(delete_old=delete_old)
    FamilyMember.refresh(delete_old=delete_old)
    FamilyMemberCompany.refresh(delete_old=delete_old)
    ConflictInterestFamilyMember.refresh(delete_old=delete_old)
    ElectionsContributionCompany.refresh(delete_old=delete_old)
    ElectionsContributionCompanyMember.refresh(delete_old=delete_old)
