"""
Module    : models
Date      : May, 2015
Author(s) : Matt Gathu <mattgathu@gmail.com>
Desc      : Veritza serbia models

"""
# ============================================================================
# necessary imports
# ============================================================================
from django.db import models
from django.db.models.signals import post_save
from django.core.management import call_command
import watson

from apps.corex import models as cmodels
from apps.corex.models import send_email_notification
from apps.corex.models import UnsavedForeignKey, UnsavedManyToManyField


# ============================================================================
# utility function(s)
# ============================================================================
def ack_save(sender, **kwargs):
    """acknowledge model save if successful"""
    if kwargs['created']:
        call_command('integratedata')


# ============================================================================
# database models definitions
# ============================================================================
class Company(cmodels.CompanyBaseModel):
    """Serbia business model """
    area = models.CharField(max_length=255)
    company_id = models.CharField(max_length=255)
    founder_number = models.CharField(max_length=255)
    legal_rep = models.CharField(max_length=255, null=True)
    members = models.CharField(max_length=255, null=True)
    place = models.CharField(max_length=255)
    tax_number = models.CharField(max_length=255)
    termination_date = models.CharField(max_length=255)
    officials = UnsavedManyToManyField('Official', blank=True)
    other_individuals = models.CharField(max_length=255, null=True)
    supervisors = models.CharField(max_length=255, null=True)

    @property
    def individuals(self):
        """get a list of company individuals"""
        individuals = [self.directors, self.founders, self.legal_rep,
                       self.members, self.other_individuals, self.supervisors]
        individuals = (x for x in individuals if x)

        return set(individuals)

    def __unicode__(self):
        return self.name

    class Meta:
        """extra options"""
        verbose_name_plural = 'Companies'


class Procurement(cmodels.ProcurementBaseModel):
    """Serbia procurement model"""
    contracting_auth_address = models.CharField(max_length=255, blank=True, verbose_name='Contracting Authority Address')
    contracting_auth_id = models.CharField(max_length=255, blank=True, verbose_name='Contracting Authority ID')
    default_reason = models.CharField(max_length=255, blank=True, verbose_name='Reason of Failure')
    orn_code = models.CharField(max_length=255, blank=True, verbose_name='ORN Code')
    lpp_basis = models.CharField(max_length=255, blank=True, verbose_name='basis of LPP')
    ppo_reviews = models.CharField(max_length=255, blank=True, verbose_name='PPO reviews')
    procedure_type = models.CharField(max_length=255, blank=True, verbose_name='Procedure type')
    subject = models.CharField(max_length=255, blank=True, verbose_name='Procurement Subject')
    purchases_val_contract = models.CharField(max_length=255, blank=True, verbose_name='Contract value of purchases')
    purchases_val_estimate = models.CharField(max_length=255, blank=True, verbose_name='Estimate value of purchases')
    offers = models.CharField(max_length=255, blank=True, verbose_name='Offers')
    selection_criterion = models.CharField(max_length=255, blank=True, verbose_name='Criterion of selection')
    preparing_bids_cost = models.CharField(max_length=255, blank=True, verbose_name='Cost of Preparing bids')
    execution_date = models.DateField(null=True, verbose_name='Date of execution / non-execution')
    execution_value = models.CharField(max_length=255, blank=True, verbose_name='Execution of contract value excl. VAT')
    eq_price = models.CharField(max_length=255, blank=True, verbose_name='Eq. price')
    execution_note = models.CharField(max_length=255, blank=True, verbose_name='Execution / non-execution note')
    cases_types = models.CharField(max_length=255, blank=True, verbose_name='Types of cases procurement')
    supplier_name = models.CharField(max_length=255, blank=True, verbose_name='Name of Vendor/Supplier')
    supplier_id = models.CharField(max_length=255, blank=True, verbose_name='Vendor/Supplier ID')
    supplier_country = models.CharField(max_length=255, blank=True, verbose_name="Vendor's Country")
    modifications = models.CharField(max_length=255, blank=True, verbose_name='Changes')

    def __unicode__(self):
        return self.contracting_auth

    class Meta:
        """extra options"""
        verbose_name_plural = 'Procurements'


class Official(cmodels.OfficialBaseModel):
    """Serbia public official model."""
    deposits_savings = models.NullBooleanField()
    place = models.CharField(max_length=255, blank=True)
    date = models.DateField(max_length=255, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        """extra options"""
        verbose_name_plural = 'Officials'


class FixedAsset(cmodels.OfficialMovable):
    """Serbia public official fixed asset"""
    official = UnsavedForeignKey('Official', null=True)
    acquisition_basis = models.CharField(max_length=255)
    ownership_stake = models.CharField(max_length=255)
    type_size = models.CharField(max_length=255)


class RealEstate(cmodels.OfficialRealEstate):
    """Serbia public official real estate asset"""
    official = UnsavedForeignKey('Official', null=True)
    place = models.CharField(max_length=255)
    structure = models.CharField(max_length=255)
    allocation_basis = models.CharField(max_length=255)
    closing_date = models.CharField(max_length=255)


class Salary(cmodels.OfficialSalary):
    """Serbia public official salary"""
    official = UnsavedForeignKey('Official', null=True)
    authority = models.CharField(max_length=255)
    currency = models.CharField(max_length=255)
    income_source = models.CharField(max_length=255)
    interval = models.CharField(max_length=255)
    net_income = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    time_period = models.CharField(max_length=255)


class Transport(cmodels.OfficialMovable):
    """Serbia public offcial transport"""
    official = UnsavedForeignKey('Official', null=True)
    acquisition_basis = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    year = models.CharField(max_length=255)


class ElectionDonation(cmodels.ElectionDonationBaseModel):
    """Serbia Election Donations """
    donation = models.CharField(max_length=255, null=True)
    dues = models.CharField(max_length=255, null=True)
    kind_donations = models.CharField(max_length=255, null=True)
    selection = models.CharField(max_length=255, null=True)

    def __unicode__(self):
        return self.donor_name

    class Meta:
        """extra options"""
        verbose_name_plural = 'Election Donations'


# ============================================================================
# veritza data integration models
# ============================================================================
class OfficialCompany(cmodels.BaseModel):
    """Public Officials and Companies data integration

    """
    official = models.ForeignKey('Official')
    company = models.ForeignKey('Company')

    def __repr__(self):
        return "{} - {}".format(self.official.name, self.company.name)

    class Meta:
        unique_together = ('official', 'company')
        verbose_name = "Public Official's company"
        verbose_name_plural = "Public Officials Companies"


class OfficialCompanyProcurement(cmodels.BaseModel):
    """Public Official Companies in Procurement

    """
    official = models.ForeignKey('Official')
    company = models.ForeignKey('Company')
    procurement = models.ForeignKey('Procurement')

    def __repr__(self):
        return "{} - {} - {}".format(self.official.name, self.company.name,
                                     self.procurement.id)

    class Meta:
        verbose_name = "Public Official's Company in Procurement"
        verbose_name_plural = "Public Officials Companies in Procurement"


class FunderCompany(cmodels.BaseModel):
    """Companies Owned by political funders

    """
    company = models.ForeignKey('Company')
    donation = models.ForeignKey('ElectionDonation')


class FunderCompanyProcurement(cmodels.BaseModel):
    """Companies Owned by political funders that are in procurement

    """
    company = models.ForeignKey('FunderCompany')
    procurement = models.ForeignKey('Procurement')


class FundingCompany(cmodels.BaseModel):
    """companies that are political funders

    """
    company = models.ForeignKey('Company')
    donation = models.ForeignKey('ElectionDonation')


class FundingCompanyProcurement(cmodels.BaseModel):
    """Companies that are political funders and also in procurement

    """
    company = models.ForeignKey('FundingCompany')
    procurement = models.ForeignKey('Procurement')

# ============================================================================
# hook up post_save signal to reciever
# ============================================================================
post_save.connect(ack_save, sender=Official, dispatch_uid="integrate_data")
post_save.connect(send_email_notification)


# ============================================================================
# register models for django-watson
# ============================================================================
for model in (Company, Procurement, Official, ElectionDonation):
    watson.register(model)


# ============================================================================
# EOF
# ============================================================================
