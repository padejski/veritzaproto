"""
Serbia tables
"""
# ============================================================================
# necessary imports
# ============================================================================
import django_tables2 as tables
from django_tables2.utils import A

from . import models


class CompanyTable(tables.Table):
    """companies data table"""
    alt_name = tables.LinkColumn('serbia:company', args=[A('pk')])
    url = tables.URLColumn()

    class Meta:
        model = models.Company
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = ('id', 'created', 'updated', 'hash', 'name', 'directors',
                   'address', 'duns_num',  'status', 'url', 'basemodel_ptr',
                   'companybasemodel_ptr', 'other', 'alt_address', 'industry')


class ElectionDonationTable(tables.Table):
    """election donations data table"""
    donor_name = tables.LinkColumn('serbia:electioncontrib', args=[A('pk')])
    url = tables.URLColumn()

    class Meta:
        model = models.ElectionDonation
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = ('id', 'created', 'updated', 'hash', 'other_donor',
                   'donor_address', 'donor_type', 'candidate', 'date',
                   'url', 'basemodel_ptr', 'electiondonationbasemodel_ptr',
                   'other', 'alt_address', 'industry')


class OfficialTable(tables.Table):
    """public officials table"""
    name = tables.LinkColumn('serbia:official', args=[A('pk')])
    url = tables.URLColumn()

    class Meta:
        model = models.Official
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = ('id', 'created', 'updated', 'hash', 'real_estates',
                   'movables', 'companies',  'children', 'spouse', 'url',
                   'basemodel_ptr', 'officialbasemodel_ptr', 'other')


class ProcurementTable(tables.Table):
    """public procurement table"""
    contracting_auth = tables.LinkColumn('serbia:procurement', args=[A('pk')])
    url = tables.URLColumn()

    class Meta:
        model = models.Procurement
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = ('id', 'created', 'updated', 'hash', 'contact_person',
                   'contracting_auth_address', 'contracting_auth_id',
                   'default_reason', 'modifications', 'cases_types',
                   'transaction_id', 'url', 'subject', 'supplier_id',
                   'supplier_country', 'preparing_bids_cost', 'eq_price',
                   'vendor', 'lpp_basis', 'ppo_reviews', 'orn_code',
                   'purchases_val_contract', 'purchases_val_estimate',
                   'offers', 'execution_date', 'execution_value',
                   'basemodel_ptr', 'procurementbasemodel_ptr', 'other')

# ============================================================================
# EOF
# ============================================================================
