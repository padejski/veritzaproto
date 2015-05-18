"""
Serbia tables
"""
# ============================================================================
# necessary imports
# ============================================================================
import django_tables2 as tables

from . import models


class CompanyTable(tables.Table):
    """companies data table"""
    class Meta:
        model = models.FedCompany
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = ('id', 'created', 'updated', 'hash', 'name', 'directors',
                   'address', 'duns_num',  'status', 'url', 'basemodel_ptr',
                   'companybasemodel_ptr', 'other', 'alt_address', 'industry')


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
    class Meta:
        model = models.FedProcurement
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = ('id', 'created', 'updated', 'hash', 'transaction_id',
                   'contact_person', 'basemodel_ptr', 'url'
                   'procurementbasemodel_ptr', 'other')


# ============================================================================
# EOF
# ============================================================================
