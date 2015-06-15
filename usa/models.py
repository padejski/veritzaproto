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


class FedIrsExemptOrg(cmodels.BaseModel):
    """IRS Exempt Organizations"""
    city = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    ein = models.CharField(max_length=255, null=True, verbose_name='EIN')
    name = models.CharField(max_length=255, null=True, verbose_name='Legal Name')
    state = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True, verbose_name='Deductibility Status')


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


class FedToxicsFacility(cmodels.BaseModel):
    """Federal Toxics Facility Model"""
    accuracy_value = models.CharField(max_length=255, null=True)
    census_block_code = models.CharField(max_length=255, null=True)
    city_name = models.CharField(max_length=255, null=True, verbose_name='City')
    collect_desc = models.CharField(max_length=255, null=True)
    congressional_dist_num = models.CharField(max_length=255, null=True, verbose_name='')
    conveyor = models.CharField(max_length=255, null=True)
    country_name = models.CharField(max_length=255, null=True, verbose_name='Country')
    county_name = models.CharField(max_length=255, null=True, verbose_name='County')
    create_date = models.CharField(max_length=255, null=True, verbose_name='Creation Date')
    epa_region_code = models.CharField(max_length=255, null=True, verbose_name='EPA Region Code')
    federal_agency_name = models.CharField(max_length=255, null=True, verbose_name='Agency')
    federal_facility_code = models.CharField(max_length=255, null=True, verbose_name='Facility Code')
    fips_code = models.CharField(max_length=255, null=True, verbose_name='FIPS Code')
    frs_facility_detail_report_url = models.CharField(max_length=255, null=True, verbose_name='Report URL')
    hdatum_desc = models.CharField(max_length=255, null=True)
    huc_code = models.CharField(max_length=255, null=True, verbose_name='HUC Code')
    interest_types = models.CharField(max_length=255, null=True)
    latitude83 = models.CharField(max_length=255, null=True)
    location_address = models.CharField(max_length=255, null=True, verbose_name='Location')
    location_description = models.CharField(max_length=255, null=True)
    longitude83 = models.CharField(max_length=255, null=True)
    naics_code_descriptions = models.CharField(max_length=255, null=True)
    naics_codes = models.CharField(max_length=255, null=True)
    pgm_sys_acrnms = models.CharField(max_length=255, null=True)
    postal_code = models.CharField(max_length=255, null=True)
    primary_name = models.CharField(max_length=255, null=True, verbose_name='Primary Name')
    ref_point_desc = models.CharField(max_length=255, null=True)
    registry_id = models.CharField(max_length=255, null=True, verbose_name='Registry ID')
    sic_code_descriptions = models.CharField(max_length=255, null=True)
    sic_codes = models.CharField(max_length=255, null=True)
    site_type_name = models.CharField(max_length=255, null=True)
    source_desc = models.CharField(max_length=255, null=True)
    state_code = models.CharField(max_length=255, null=True)
    state_name = models.CharField(max_length=255, null=True, verbose_name='State')
    supplemental_location = models.CharField(max_length=255, null=True)
    tribal_land_code = models.CharField(max_length=255, null=True)
    tribal_land_name = models.CharField(max_length=255, null=True, verbose_name='Tribal Land Name')
    update_date = models.CharField(max_length=255, null=True, verbose_name='Update Date')
    us_mexico_border_ind = models.CharField(max_length=255, null=True)


class FedOshaEbsa(cmodels.BaseModel):
    """Federal OSHA EBSA Enforcement Data"""
    case_type = models.CharField(max_length=255, null=True, verbose_name='Case Type')
    ein = models.CharField(max_length=255, null=True, verbose_name='EIN')
    final_close_date = models.CharField(max_length=255, null=True, verbose_name='Closing Date')
    final_close_reason = models.CharField(max_length=255, null=True, verbose_name='Closing Reason')
    penalty_amount = models.CharField(max_length=255, null=True, verbose_name='Penalty Amount')
    plan_admin = models.CharField(max_length=255, null=True, verbose_name='Administrator')
    plan_admin_state = models.CharField(max_length=255, null=True, verbose_name='Admin State')
    plan_admin_zip_code = models.CharField(max_length=255, null=True, verbose_name='Admin Zip Code')
    plan_name = models.CharField(max_length=255, null=True, verbose_name='Plan Name')
    plan_year = models.CharField(max_length=255, null=True, verbose_name='Plan Year')
    pn = models.CharField(max_length=255, null=True, verbose_name='Plan Number')


class FedOshaInspection(cmodels.BaseModel):
    """Federal OSHA Inspection Data"""
    activity_nr = models.CharField(max_length=255, null=True, verbose_name='Inspection ID')
    adv_notice = models.CharField(max_length=255, null=True, verbose_name='Advance Notice')
    case_mod_date = models.CharField(max_length=255, null=True)
    close_case_date = models.CharField(max_length=255, null=True)
    close_conf_date = models.CharField(max_length=255, null=True)
    estab_name = models.CharField(max_length=255, null=True, verbose_name='Establishment Name')
    health_const = models.CharField(max_length=255, null=True)
    health_manuf = models.CharField(max_length=255, null=True)
    health_marit = models.CharField(max_length=255, null=True)
    host_est_key = models.CharField(max_length=255, null=True)
    indstry_dim_id = models.CharField(max_length=255, null=True)
    insp_scope = models.CharField(max_length=255, null=True)
    insp_type = models.CharField(max_length=255, null=True)
    ld_dt = models.CharField(max_length=255, null=True)
    mail_city = models.CharField(max_length=255, null=True)
    mail_state = models.CharField(max_length=255, null=True)
    mail_street = models.CharField(max_length=255, null=True)
    mail_zip = models.CharField(max_length=255, null=True)
    migrant = models.CharField(max_length=255, null=True)
    naics_code = models.CharField(max_length=255, null=True, verbose_name='NAICS Code')
    nr_in_estab = models.CharField(max_length=255, null=True)
    open_date = models.CharField(max_length=255, null=True)
    owner_code = models.CharField(max_length=255, null=True, verbose_name='Owner Code')
    owner_type = models.CharField(max_length=255, null=True)
    reporting_id = models.CharField(max_length=255, null=True)
    safety_const = models.CharField(max_length=255, null=True)
    safety_hlth = models.CharField(max_length=255, null=True)
    safety_manuf = models.CharField(max_length=255, null=True)
    safety_marit = models.CharField(max_length=255, null=True)
    sic_code = models.CharField(max_length=255, null=True)
    site_address = models.CharField(max_length=255, null=True)
    site_city = models.CharField(max_length=255, null=True, verbose_name='City')
    site_state = models.CharField(max_length=255, null=True, verbose_name='State')
    site_zip = models.CharField(max_length=255, null=True, verbose_name='ZIP')
    state_flag = models.CharField(max_length=255, null=True)
    union_status = models.CharField(max_length=255, null=True)
    why_no_insp = models.CharField(max_length=255, null=True, verbose_name='No Inspection Reason')
    zip_dim_id = models.CharField(max_length=255, null=True)


class FedCpscRecall(cmodels.BaseModel):
    """Federal Consumer Product Safety Commission Recall Model"""
    consumer_contact = models.CharField(max_length=255, null=True, verbose_name='Consumer Contact')
    desc = models.CharField(max_length=255, null=True)
    hazards = models.CharField(max_length=255, null=True)
    images = models.CharField(max_length=255, null=True)
    in_conj = models.CharField(max_length=255, null=True)
    injuries = models.CharField(max_length=255, null=True)
    last_pub_date = models.CharField(max_length=255, null=True)
    mfcs_countries = models.CharField(max_length=255, null=True)
    mfcs = models.CharField(max_length=255, null=True, verbose_name='Manufacturers')
    products = models.CharField(max_length=255, null=True)
    product_upcs = models.CharField(max_length=255, null=True)
    recall_date = models.CharField(max_length=255, null=True)
    recall_id = models.CharField(max_length=255, null=True)
    recall_num = models.CharField(max_length=255, null=True)
    remedies = models.CharField(max_length=255, null=True)
    retailers = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255, null=True)
    url = models.CharField(max_length=255, null=True)


class FedCpscRecallViolation(cmodels.BaseModel):
    """Federal Conusmer Product Safety Comm. Recall Violation Model"""
    action_requested = models.CharField(max_length=255, null=True, verbose_name='Action Requested')
    address_1 = models.CharField(max_length=255, null=True, verbose_name='Address')
    address_2 = models.CharField(max_length=255, null=True)
    citation = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    firm = models.CharField(max_length=255, null=True)
    foreign_mfg = models.CharField(max_length=255, null=True, verbose_name='Foreign Manufacturing')
    loa_date = models.CharField(max_length=255, null=True, verbose_name='LOA Date')
    lot_size = models.CharField(max_length=255, null=True, verbose_name='Lot Size')
    model = models.CharField(max_length=255, null=True)
    primary_violation = models.CharField(max_length=255, null=True, verbose_name='Primary Violation')
    product = models.CharField(max_length=255, null=True)


# ============================================================================
# EOF
# ============================================================================
