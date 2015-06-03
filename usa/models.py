"""
Module    : models
Date      : May, 2015
Author(s) : Matt Gathu <mattgathu@gmail.com>
Desc      : Veritza usa models

"""
# ============================================================================
# necessary imports
# ============================================================================
from django.db import models
from corex import models as cmodels


# ============================================================================
# database models definitions
# ============================================================================
class FedCompany(cmodels.CompanyBaseModel):
    """Federal company model """
    place = models.CharField(max_length=255)

    class Meta:
        """extra options"""
        verbose_name_plural = "Federal Companies"


class FedProcurement(cmodels.ProcurementBaseModel):
    """Federal Procurement model

    """
    class Meta:
        """extra options"""
        verbose_name_plural = 'Procurements'


class FedFinancialDisclosure(cmodels.BaseModel):
    """Federal Financial Disclosure model """
    filing = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    office = models.CharField(max_length=255)
    pdf = models.CharField(max_length=255)
    year = models.CharField(max_length=255)

# ============================================================================
# EOF
# ============================================================================
