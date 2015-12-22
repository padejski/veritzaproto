"""
Module    : models
Date      : May, 2015
Author(s) : Matt Gathu <mattgathu@gmail.com>
Desc      : Veritza core models

"""
# ============================================================================
# imports
# ============================================================================
from django.db import models


# ============================================================================
# custom db fields
# ============================================================================
class UnsavedForeignKey(models.ForeignKey):
    """An FK which can point to a unsaved obj"""
    allow_unsaved_instance_assignment = True


class UnsavedManyToManyField(models.ManyToManyField):
    """A M2M field which can point to a unsaved obj"""
    allow_unsaved_instance_assignment = True


# ============================================================================
# core database models
# ============================================================================
class BaseModel(models.Model):
    """base model"""
    id = models.AutoField(primary_key=True)
    hash = models.CharField(max_length=255, unique=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    @classmethod
    def get_url_name(cls):
        return cls._meta.verbose_name_plural.replace(' ', '-').lower()


class CompanyBaseModel(BaseModel):
    """Company base model"""
    name = models.CharField(max_length=255)
    alt_name = models.CharField(max_length=255, verbose_name='name', null=True)
    founders = models.CharField(max_length=255, null=True)
    directors = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, null=True)
    industry = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    alt_address = models.CharField(max_length=255, null=True)
    reg_date = models.DateField(null=True)
    status = models.CharField(max_length=255, null=True)
    duns_num = models.CharField(max_length=255, null=True)
    other = models.CharField(max_length=255, null=True)
    url = models.URLField(max_length=255, null=True)


class OfficialBaseModel(BaseModel):
    """Public official base model"""
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True)
    year = models.CharField(max_length=255, blank=True)
    other = models.CharField(max_length=255, blank=True)
    url = models.URLField(max_length=255, blank=True)


class OfficialSpouse(BaseModel):
    """Public official's spouse model"""
    name = models.CharField(max_length=255, blank=True)


class OfficialChild(BaseModel):
    """Public official's child model"""
    name = models.CharField(max_length=255, blank=True)
    job = models.CharField(max_length=255, blank=True)
    salary = models.CharField(max_length=255, blank=True)
    real_estate = models.CharField(max_length=255, blank=True)
    movables = models.CharField(max_length=255, blank=True)
    companies = models.CharField(max_length=255, blank=True)


class OfficialMovable(BaseModel):
    """Public official movable property"""


class OfficialRealEstate(BaseModel):
    """Public official real estate model"""


class OfficialSalary(BaseModel):
    """public official salary model"""


class ProcurementBaseModel(BaseModel):
    """Procurement base model

    """
    contact_person = models.CharField(max_length=255, null=True)
    contracting_auth = models.CharField(max_length=255, null=True, verbose_name='Contracting Authority')
    date = models.DateField(null=True, verbose_name='Contract Date')
    desc = models.CharField(max_length=255, null=True, verbose_name='Description')
    year = models.CharField(max_length=255, null=True)
    place = models.CharField(max_length=255, null=True)
    price = models.CharField(max_length=255, null=True)
    transaction_id = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, null=True)
    url = models.URLField(max_length=255, null=True)
    vendor = UnsavedForeignKey('CompanyBaseModel', null=True)
    other = models.CharField(max_length=255, null=True)


class ElectionDonationBaseModel(BaseModel):
    """Election donation base model

    """
    date = models.CharField(max_length=255, null=True)
    donor_name = models.CharField(max_length=255, null=True, verbose_name='Donor Name')
    donor_address = models.CharField(max_length=255, null=True, verbose_name='Donor Address')
    donor_type = models.CharField(max_length=255, null=True, verbose_name='Donor Type')
    other_donor = models.CharField(max_length=255, null=True, verbose_name='Other Donor')
    candidate = models.CharField(max_length=255, null=True)
    political_party = models.CharField(max_length=255, null=True, verbose_name='Political Party')
    election_type = models.CharField(max_length=255, null=True, verbose_name='Election Type')
    amount = models.CharField(max_length=255, null=True)
    other = models.CharField(max_length=255, null=True)
    url = models.CharField(max_length=255, null=True)


class ScrapeTracker(models.Model):
    """Scraper tracker

    """
    id = models.AutoField(primary_key=True)
    last_run = models.DateTimeField(auto_now_add=True, null=True)
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=50, default='pending')
# ============================================================================
# EOF
# ============================================================================
