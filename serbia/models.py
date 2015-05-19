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
from corex import models as cmodels
from corex.models import UnsavedForeignKey, UnsavedManyToManyField


# ============================================================================
# database models definitions
# ============================================================================
class Company(cmodels.CompanyBaseModel):
    """Serbia business model """
    area = models.CharField(max_length=255)
    company_id = models.CharField(max_length=255)
    form = models.CharField(max_length=255)
    founder_number = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    tax_number = models.CharField(max_length=255)
    termination_date = models.CharField(max_length=255)
    officials = UnsavedManyToManyField('Official')

    class Meta:
        """extra options"""
        verbose_name_plural = 'Companies'


class Official(cmodels.OfficialBaseModel):
    """Serbia public official model."""
    deposits_savings = models.NullBooleanField()
    place = models.CharField(max_length=255, blank=True)
    date = models.DateField(max_length=255, null=True)

    class Meta:
        """extra options"""
        verbose_name_plural = 'Public Officials'


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
# ============================================================================
# EOF
# ============================================================================
