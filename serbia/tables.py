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
        model = models.Company
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = ('id', 'created', 'updated', 'hash', 'name', 'directors',
                   'address', 'duns_num',  'status', 'url', 'basemodel_ptr',
                   'companybasemodel_ptr', 'other', 'alt_address', 'industry')


class OfficialTable(tables.Table):
    """public officials table"""
    class Meta:
        model = models.Official
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = ('id', 'created', 'updated', 'hash', 'real_estates',
                   'movables', 'companies',  'children', 'spouse', 'url',
                   'basemodel_ptr', 'officialbasemodel_ptr', 'other')

# ============================================================================
# EOF
# ============================================================================
