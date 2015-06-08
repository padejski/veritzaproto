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
class FedCandidate(cmodels.BaseModel):
    """Candidate model"""
    cand_id = models.CharField(max_length=255, null=True)
    cand_name = models.CharField(max_length=255, null=True, verbose_name='Name')
    cand_pty_affiliation = models.CharField(max_length=255, null=True, verbose_name='Party Affiliation')
    cand_election_yr = models.CharField(max_length=255, null=True, verbose_name='Election Year')
    cand_office_st = models.CharField(max_length=255, null=True, verbose_name='Office State')
    cand_office = models.CharField(max_length=255, null=True, verbose_name='Office')
    cand_office_district = models.CharField(max_length=255, null=True, verbose_name='District')
    cand_ici = models.CharField(max_length=255, null=True, verbose_name='Incumbent Challenger Status')
    cand_status = models.CharField(max_length=255, null=True, verbose_name='Status')
    cand_pcc = models.CharField(max_length=255, null=True, verbose_name='Campaign Committee')
    cand_st1 = models.CharField(max_length=255, null=True, verbose_name='Street')
    cand_st2 = models.CharField(max_length=255, null=True, verbose_name='Street2')
    cand_city = models.CharField(max_length=255, null=True, verbose_name='City')
    cand_st = models.CharField(max_length=255, null=True, verbose_name='State')
    cand_zip = models.CharField(max_length=255, null=True, verbose_name='Zip Code')


class FedCompany(cmodels.CompanyBaseModel):
    """Federal company model """
    place = models.CharField(max_length=255)

    class Meta:
        """extra options"""
        verbose_name_plural = "Federal Companies"


class FedCommitteeContribution(cmodels.BaseModel):
    """Committee Election Contribution Model"""
    amndt_ind = models.CharField(max_length=255, null=True, verbose_name='Amendment')
    cand_id = models.CharField(max_length=255, null=True, verbose_name='Candidate')
    city = models.CharField(max_length=255, null=True)
    cmte_id = models.CharField(max_length=255, null=True, verbose_name='Committee ID')
    employer = models.CharField(max_length=255, null=True)
    entity_tp = models.CharField(max_length=255, null=True, verbose_name='Entity Type')
    file_num = models.CharField(max_length=255, null=True, verbose_name='File Number')
    image_num = models.CharField(max_length=255, null=True, verbose_name='Microfilm Location')
    memo_cd = models.CharField(max_length=255, null=True, verbose_name='Memo Code')
    memo_text = models.CharField(max_length=255, null=True, verbose_name='Memo Text')
    name = models.CharField(max_length=255, null=True, verbose_name='Contributor Name')
    occupation = models.CharField(max_length=255, null=True)
    other_id = models.CharField(max_length=255, null=True, verbose_name='Other ID')
    rpt_tp = models.CharField(max_length=255, null=True, verbose_name='Report Type')
    state = models.CharField(max_length=255, null=True)
    sub_id = models.CharField(max_length=255, null=True, verbose_name='FEC Record Number')
    tran_id = models.CharField(max_length=255, null=True, verbose_name='Transaction ID')
    transaction_amt = models.CharField(max_length=255, null=True, verbose_name='Transaction Amount')
    transaction_dt = models.CharField(max_length=255, null=True, verbose_name='Transaction Date')
    transaction_pgi = models.CharField(max_length=255, null=True, verbose_name='Primary-Gen Indicator')
    transaction_tp = models.CharField(max_length=255, null=True, verbose_name='Transaction Type')
    zip_code = models.CharField(max_length=255, null=True, verbose_name='Zip Code')


class FedIndividualContribution(cmodels.BaseModel):
    """Individual Election Contribution Model"""
    cmte_id = models.CharField(max_length=255, null=True)
    amndt_ind = models.CharField(max_length=255, verbose_name='Amendment', null=True)
    rpt_tp = models.CharField(max_length=255, verbose_name='Report Type', null=True)
    transaction_pgi = models.CharField(max_length=255, verbose_name='Primary-General Indicator', null=True)
    image_num = models.CharField(max_length=255, verbose_name='Microfilm Location', null=True)
    transaction_tp = models.CharField(max_length=255, verbose_name='Transaction Type', null=True)
    entity_tp = models.CharField(max_length=255, verbose_name='Entity Type', null=True)
    name = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    zip_code = models.CharField(max_length=255, verbose_name='Zip Code', null=True)
    employer = models.CharField(max_length=255, null=True)
    occupation = models.CharField(max_length=255, null=True)
    transaction_dt = models.CharField(max_length=255, verbose_name='Date', null=True)
    transaction_amt = models.CharField(max_length=255, verbose_name='Amount', null=True)
    other_id = models.CharField(max_length=255, verbose_name='Other ID', null=True)
    tran_id = models.CharField(max_length=255, verbose_name='Transaction ID', null=True)
    file_num = models.CharField(max_length=255, verbose_name='File Number', null=True)
    memo_cd = models.CharField(max_length=255, verbose_name='Memo Code', null=True)
    memo_text = models.CharField(max_length=255, verbose_name='Memo Text', null=True)
    sub_id = models.CharField(max_length=255, verbose_name='FEC Record Number', null=True)


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
