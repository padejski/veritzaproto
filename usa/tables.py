"""
Serbia tables
"""
# ============================================================================
# necessary imports
# ============================================================================
import django_tables2 as tables
from django_tables2.utils import A

from . import models


class CandidateTable(tables.Table):
    """election candidate table"""
    cand_name = tables.LinkColumn('usa:candidate', args=[A('pk')])
    cand_pty_affiliation = tables.Column()
    cand_election_yr = tables.Column()
    cand_office = tables.Column()

    class Meta:
        models = models.FedCandidate
        attrs = {"class": "paleblue table table-striped table-bordered"}


class CompanyTable(tables.Table):
    """companies data table"""
    name = tables.LinkColumn('usa:company', args=[A('pk')])

    class Meta:
        model = models.FedCompany
        attrs = {"class": "paleblue table table-striped table-bordered"}
        sequence = ('name', 'type', 'reg_date')
        exclude = ('id', 'alt_name', 'created', 'updated', 'hash', 'directors',
                   'address', 'duns_num',  'status', 'url', 'basemodel_ptr',
                   'place', 'companybasemodel_ptr', 'other', 'alt_address',
                   'industry')


class ElectionContributionTable(tables.Table):
    """election contributions  data table"""
    id = tables.LinkColumn('usa:econtrib', args=[A('pk')])

    class Meta:
        model = models.FedElectionContribution
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = ('created', 'updated', 'hash', 'amndt_ind', 'memo_cd',
                   'sub_id', 'transaction_pgi', 'zip_code',
                   'memo_text', 'other_id',  'status', 'url', 'basemodel_ptr',
                   'image_num', 'other', 'occupation', 'industry', 'employer',
                   'candidate', 'entity_tp', 'transaction_tp')


class FinancialDisclosureTable(tables.Table):
    """Financial disclosures  data table"""
    name = tables.LinkColumn('usa:disclosure', args=[A('pk')])
    pdf = tables.URLColumn()

    class Meta:
        model = models.FedFinancialDisclosure
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = ('id', 'created', 'updated', 'hash', 'url', 'basemodel_ptr')


class IrsExemptOrgTable(tables.Table):
    """IRS Exempt Organizations  data table"""
    id = tables.LinkColumn('usa:irsexempt', args=[A('pk')])

    class Meta:
        model = models.FedIrsExemptOrg
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = ('created', 'updated', 'hash', 'url', 'basemodel_ptr')


class OfficialTable(tables.Table):
    """public officials table"""
    class Meta:
        model = None
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = ('id', 'created', 'updated', 'hash', 'real_estates',
                   'movables', 'companies',  'children', 'spouse', 'url',
                   'basemodel_ptr', 'officialbasemodel_ptr', 'other')


class ProcurementTable(tables.Table):
    """procurements table """
    id = tables.LinkColumn('usa:procurement', args=[A('pk')])

    class Meta:
        model = models.FedProcurement
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = ('created', 'updated', 'hash', 'transaction_id', 'type',
                   'contact_person', 'basemodel_ptr', 'url', 'vendor',
                   'procurementbasemodel_ptr', 'other', 'desc', 'year')


class SecFilingTable(tables.Table):
    """SEC filings  data table"""
    id = tables.LinkColumn('usa:secfiling', args=[A('pk')])

    class Meta:
        model = models.FedSecFiling
        attrs = {"class": "paleblue table table-striped table-bordered"}
        sequence = ('id', 'company_conformed_name', 'filed_as_of_date',
                    'film_number', 'sec_file_number', 'city')
        exclude = ('created', 'updated', 'hash', 'url', 'basemodel_ptr',
                   'accession_number', 'business_phone', 'central_index_key',
                   'company_data', 'date_as_of_change', 'date_of_name_change',
                   'former_company', 'former_conformed_name', 'public_document_count',
                   'sec_act', 'standard_industrial_classification', 'street_2',
                   'zip', 'business_address', 'filer', 'fiscal_year_end', 'state',
                   'conformed_submission_type', 'mail_address', 'form_type',
                   'state_of_incorporation', 'street_1', 'filing_values',
                   'irs_number')


class ToxicsFacilityTable(tables.Table):
    """Toxics facilities  data table"""
    id = tables.LinkColumn('usa:toxicsfacility', args=[A('pk')])

    class Meta:
        model = models.FedToxicsFacility
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = ('created', 'updated', 'hash', 'url', 'basemodel_ptr',
                   'accuracy_value', 'census_block_code', 'collect_desc',
                   'congressional_dist_num', 'conveyor', 'epa_region_code',
                   'federal_facility_code', 'hdatum_desc', 'huc_code',
                   'interest_types', 'latitude83', 'location_description',
                   'longitude83', 'naics_code_descriptions', 'pgm_sys_acrnms',
                   'ref_point_desc', 'sic_code_descriptions', 'source_desc',
                   'state_code', 'supplemental_location', 'tribal_land_name',
                   'tribal_land_code', 'tribal_land_name', 'us_mexico_border_ind')


class OshaEbsaTable(tables.Table):
    """OSHA Ebsa Enforcement data table"""
    id = tables.LinkColumn('usa:oshaebsa', args=[A('pk')])

    class Meta:
        model = models.FedOshaEbsa
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = ('created', 'updated', 'hash', 'url', 'basemodel_ptr')


class OshaInspectionTable(tables.Table):
    """OSHA Inspection  data table"""
    id = tables.LinkColumn('usa:oshainsp', args=[A('pk')])

    class Meta:
        model = models.FedOshaInspection
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = ('created', 'updated', 'hash', 'url', 'basemodel_ptr',
                   'case_mod_date', 'close_case_date', 'close_conf_date',
                   'health_const', 'health_manuf', 'health_marit',
                   'host_est_key', 'indstry_dim_id', 'insp_type', 'insp_scope',
                   'ld_dt', 'mail_city', 'mail_state', 'mail_street', 'mail_zip',
                   'migrant', 'nr_in_estab', 'owner_type', 'safety_hlth',
                   'safety_const', 'safety_manuf', 'safety_marit', 'site_address',
                   'site_zip', 'state_flag', 'union_status', 'zip_dim_id')


class CpscRecallTable(tables.Table):
    """Consumer Product Safety Commission Recall data table"""
    id = tables.LinkColumn('usa:cpscrecall', args=[A('pk')])

    class Meta:
        model = models.FedCpscRecall
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = ('created', 'updated', 'hash', 'url', 'basemodel_ptr',
                   'consumer_contact', 'hazards', 'images', 'in_conj', 'injuries',
                   'mfcs_countries', 'product_upcs', 'remedies', 'desc')


class CpscRecallViolationTable(tables.Table):
    """Consumer Product Safety Commission Recall Violation data table"""
    firm = tables.LinkColumn('usa:cpscviol', args=[A('pk')])

    class Meta:
        model = models.FedCpscRecallViolation
        attrs = {"class": "paleblue table table-striped table-bordered"}
        sequence = ('firm', 'primary_violation', 'product', 'action_requested',
                    'lot_size', 'address_1')
        exclude = ('id', 'created', 'updated', 'hash', 'url', 'basemodel_ptr',
                   'address_2', 'citation', 'foreign_mfg', 'loa_date',
                   'model', 'country')


# ============================================================================
# EOF
# ============================================================================
