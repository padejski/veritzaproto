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


class FedSecFiling(cmodels.BaseModel):
    """Federal Securities and Exchange Commission filing model"""
    accession_number = models.CharField(max_length=255, null=True)
    business_address = models.CharField(max_length=255, null=True)
    business_phone = models.CharField(max_length=255, null=True)
    central_index_key = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    company_conformed_name = models.CharField(max_length=255, null=True)
    company_data = models.CharField(max_length=255, null=True)
    conformed_submission_type = models.CharField(max_length=255, null=True)
    date_as_of_change = models.CharField(max_length=255, null=True)
    date_of_name_change = models.CharField(max_length=255, null=True)
    filed_as_of_date = models.CharField(max_length=255, null=True)
    filer = models.CharField(max_length=255, null=True)
    filing_values = models.CharField(max_length=255, null=True)
    film_number = models.CharField(max_length=255, null=True)
    fiscal_year_end = models.CharField(max_length=255, null=True)
    form_type = models.CharField(max_length=255, null=True)
    former_company = models.CharField(max_length=255, null=True)
    former_conformed_name = models.CharField(max_length=255, null=True)
    irs_number = models.CharField(max_length=255, null=True)
    mail_address = models.CharField(max_length=255, null=True)
    public_document_count = models.CharField(max_length=255, null=True)
    sec_act = models.CharField(max_length=255, null=True)
    sec_file_number = models.CharField(max_length=255, null=True)
    standard_industrial_classification = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    state_of_incorporation = models.CharField(max_length=255, null=True)
    street_1 = models.CharField(max_length=255, null=True)
    street_2 = models.CharField(max_length=255, null=True)
    url = models.CharField(max_length=255, null=True)
    zip = models.CharField(max_length=255, null=True)


# ============================================================================
# EOF
# ============================================================================
