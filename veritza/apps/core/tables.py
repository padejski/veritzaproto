import django_tables2 as tables
from veritza.apps.core.models import *

class VeritzaTable(tables.Table):

    class Meta:
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok'
        )


class PublicOfficialTable(VeritzaTable):

    class Meta:
        model = PublicOfficial
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
        	'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok',
        	'system_id'
        )


class CompanyTable(VeritzaTable):

    class Meta:
        model = Company
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok',
            'mail_address', 'name',  'status', 'system_id', 'link'
        )


class CompanyMemberTable(VeritzaTable):

    class Meta:
        model = CompanyMember
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok',
            'mail_address', 'name',  'status', 'system_id', 'link'
        )
        sequence = ['first_name', 'last_name', 'company_registration_number', 'company']


class FamilyMemberTable(VeritzaTable):

    class Meta:
        model = FamilyMember
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
        	'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok',
        	'mail_address', 'name',  'status', 'system_id', 'link'
        )
        # sequence = ['first_name', 'last_name', 'company_registration_number', 'company']


class PublicProcurementTable(VeritzaTable):

    class Meta:
        model = PublicProcurement
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok'
        )

class BidderCompanyTable(VeritzaTable):

    class Meta:
        model = BidderCompany
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok'
        )

class ElectionsContributionsTable(VeritzaTable):

    class Meta:
        model = ElectionsContributions
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok'
        )

class PublicOfficialCompanyTable(VeritzaTable):

    class Meta:
        model = PublicOfficialCompany
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok'
        )

class ConflictInterestTable(VeritzaTable):

    class Meta:
        model = ConflictInterest
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
        	'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok',
        	'mail_address', 'name',  'status', 'system_id', 'link'
        )


class FamilyMemberCompanyTable(VeritzaTable):

    class Meta:
        model = FamilyMemberCompany
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok'
        )

class ConflictInterestFamilyMemberTable(VeritzaTable):

    class Meta:
        model = ConflictInterestFamilyMember
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok'
        )

