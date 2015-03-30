import django_tables2 as tables
from veritza.apps.core.models import *


class PublicOfficialTable(tables.Table):

    class Meta:
        model = PublicOfficial
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
        	'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok',
        	'system_id'
        )


class CompanyTable(tables.Table):

    class Meta:
        model = Company
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
        	'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok',
        	'mail_address', 'name',  'status', 'system_id', 'link'
        )

class ConflictInterestTable(tables.Table):

    class Meta:
        model = ConflictInterest
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
        	'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok',
        	'mail_address', 'name',  'status', 'system_id', 'link'
        )
