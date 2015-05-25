from django.utils.safestring import mark_safe
from django.utils.html import escape
from django.core.urlresolvers import reverse

import django_tables2 as tables

from veritza.apps.core.models import *

class VeritzaTable(tables.Table):

    class Meta:
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok'
        )

    def render_link(self, record, value):
        return mark_safe(u'<a href="{0}">source</a>'.format(value))

class PublicOfficialTable(VeritzaTable):

    reports = tables.Column(accessor='publicofficialreport_set')
    type = tables.Column(accessor='publicofficialreport_set')
    link = tables.Column(accessor='link')

    class Meta:
        model = PublicOfficial
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
        	'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok',
        	'system_id'
        )

    def render_name(self, record, value):
        return mark_safe(u'<a href="{0}" title="Current record details">{1}</a>'.format(
            reverse('public-officials', args=[record.id]), escape(value)
        ))

    def render_reports(self, record, value):
        return len(value.all())

    def render_type(self, record, value):
        if len(value.all()) > 0:
            return value.all()[0].official_type
        return ""

    def render_link(self, record, value):
        return mark_safe(u'<a href="{0}">source</a>'.format(value))

class CompanyTable(VeritzaTable):

    members = tables.Column(accessor='companymember_set')
    procurements = tables.Column(accessor='biddercompany_set')

    class Meta:
        model = Company
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok',
            'mail_address', 'name',  'status', 'system_id'
        )

    def render_registration_number(self, record, value):
        return mark_safe(u'<a href="{0}" title="Current record details">{1}</a>'.format(
            reverse('companies', args=[record.id]), escape(value)
        ))

    def render_members(self, record, value):
        return len(value.all())

    def render_procurements(self, record, value):
        return len(value.all())


class CompanyMemberTable(VeritzaTable):

    class Meta:
        model = CompanyMember
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok',
            'mail_address', 'name',  'status', 'system_id', 'company_registration_number'
        )
        sequence = ['id', 'first_name', 'last_name', 'company']


    def render_id(self, record, value):
        return mark_safe(u'<a href="{0}" title="Current record details">{1}</a>'.format(
            reverse('company-members', args=[record.id]), escape(value)
        ))

    def render_company(self, record, value):
        return mark_safe(u'<a href="{0}" title="Company details">{1}</a>'.format(
            reverse('companies', args=[record.company.id]), escape(value)
        ))


class FamilyMemberTable(VeritzaTable):

    class Meta:
        model = FamilyMember
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
        	'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok',
        	'mail_address',  'status', 'system_id'
        )

        sequence = ['name', 'public_official', 'relationship']


    def render_name(self, record, value):
        return mark_safe(u'<a href="{0}" title="Current record details">{1}</a>'.format(
            reverse('family-members', args=[record.id]), escape(value)
        ))

    def render_public_official(self, record, value):
        return mark_safe(u'<a href="{0}" title="Official details">{1}</a>'.format(
            reverse('public-officials', args=[record.public_official.id]), escape(value)
        ))


class PublicProcurementTable(VeritzaTable):
    winner = tables.Column(accessor='link', verbose_name='Winner')

    class Meta:
        model = PublicProcurement
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok',
            'system_id', 'record_type'
        )

    def render_number(self, record, value):
        return mark_safe(u'<a href="{0}" title="Current record details">{1}</a>'.format(
            reverse('public-procurements', args=[record.id]), escape(value)
        ))

    def render_value(self, record, value):
        return mark_safe(u'{0} &euro;'.format(value))

    def render_winner(self, record, value):
        if record.biddercompany_set.all():
            winner = record.biddercompany_set.all()[0].company
            return mark_safe(u'<a href="{0}">{1}</a>'.format(reverse('companies', args=[winner.id]), winner.name))
        return ""

class BidderCompanyTable(VeritzaTable):

    class Meta:
        model = BidderCompany
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok'
        )

    def render_id(self, record, value):
        return mark_safe(u'<a href="{0}" title="Current record details">{1}</a>'.format(
            reverse('bidder-companies', args=[record.id]), escape(value)
        ))

    def render_company(self, record, value):
        return mark_safe(u'<a href="{0}" title="Company details">{1}</a>'.format(
            reverse('companies', args=[record.company.id]), escape(value)
        ))

    def render_procurement(self, record, value):
        return mark_safe(u'<a href="{0}" title="Procurement details">{1}</a>'.format(
            reverse('public-procurements', args=[record.procurement.id]), escape(value)
        ))


class ElectionsContributionsTable(VeritzaTable):

    class Meta:
        model = ElectionsContributions
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok', 'csv_file'
        )

    def render_id(self, record, value):
        return mark_safe(u'<a href="{0}" title="Current record details">{1}</a>'.format(
            reverse('elections-contributions', args=[record.id]), escape(value)
        ))

    def render_amount(self, record, value):
        return mark_safe(u'{0} &euro;'.format(value))


class PublicOfficialCompanyTable(VeritzaTable):

    class Meta:
        model = PublicOfficialCompany
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok'
        )

    def render_id(self, record, value):
        return mark_safe(u'<a href="{0}" title="Current record details">{1}</a>'.format(
            reverse('public-official-companies', args=[record.id]), escape(value)
        ))

    def render_official(self, record, value):
        return mark_safe(u'<a href="{0}" title="Official details">{1}</a>'.format(
            reverse('public-officials', args=[record.official.id]), escape(value)
        ))

    def render_company(self, record, value):
        return mark_safe(u'<a href="{0}" title="Company details">{1}</a>'.format(
            reverse('companies', args=[record.company.id]), escape(value)
        ))


class ConflictInterestTable(VeritzaTable):

    class Meta:
        model = ConflictInterest
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
        	'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok',
        	'mail_address', 'name',  'status', 'system_id', 'link'
        )


    def render_id(self, record, value):
        return mark_safe(u'<a href="{0}" title="Current record details">{1}</a>'.format(
            reverse('public-official-companies', args=[record.id]), escape(value)
        ))

    def render_official(self, record, value):
        return mark_safe(u'<a href="{0}" title="Official details">{1}</a>'.format(
            reverse('public-officials', args=[record.official.id]), escape(value)
        ))

    def render_company(self, record, value):
        return mark_safe(u'<a href="{0}" title="Company details">{1}</a>'.format(
            reverse('companies', args=[record.company.id]), escape(value)
        ))

    def render_public_procurement(self, record, value):
        return mark_safe(u'<a href="{0}" title="Procurement details">{1}</a>'.format(
            reverse('public-procurements', args=[record.public_procurement.id]), escape(value)
        ))


class FamilyMemberCompanyTable(VeritzaTable):

    class Meta:
        model = FamilyMemberCompany
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok'
        )

    def render_id(self, record, value):
        return mark_safe(u'<a href="{0}" title="Current record details">{1}</a>'.format(
            reverse('companies', args=[record.id]), escape(value)
        ))

    def render_member(self, record, value):
        return mark_safe(u'<a href="{0}" title="Family member details">{1}</a>'.format(
            reverse('family-members', args=[record.member.id]), escape(value)
        ))

    def render_company(self, record, value):
        return mark_safe(u'<a href="{0}" title="Company details">{1}</a>'.format(
            reverse('companies', args=[record.company.id]), escape(value)
        ))



class ConflictInterestFamilyMemberTable(VeritzaTable):

    class Meta:
        model = ConflictInterestFamilyMember
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok'
        )

    def render_id(self, record, value):
        return mark_safe(u'<a href="{0}" title="Current record details">{1}</a>'.format(
            reverse('public-official-companies', args=[record.id]), escape(value)
        ))

    def render_member(self, record, value):
        return mark_safe(u'<a href="{0}" title="Official details">{1}</a>'.format(
            reverse('family-members', args=[record.member.id]), escape(value)
        ))

    def render_company(self, record, value):
        return mark_safe(u'<a href="{0}" title="Company details">{1}</a>'.format(
            reverse('companies', args=[record.company.id]), escape(value)
        ))

    def render_public_procurement(self, record, value):
        return mark_safe(u'<a href="{0}" title="Procurement details">{1}</a>'.format(
            reverse('public-procurements', args=[record.public_procurement.id]), escape(value)
        ))
