from django.utils.safestring import mark_safe
from django.utils.html import escape
from django.core.urlresolvers import reverse

import django_tables2 as tables

from apps.core import models


class VeritzaTable(tables.Table):

    class Meta:
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok'
        )

    def render_link(self, record, value):
        return mark_safe(u'<a href="{0}">source</a>'.format(value))


class PublicOfficialTable(VeritzaTable):

    reports = tables.Column(accessor='reports')
    year = tables.Column(accessor='reports')
    type = tables.Column(accessor='reports')
    position = tables.Column(accessor='reports')
    link = tables.Column(accessor='link')

    class Meta:
        model = models.PublicOfficial
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok',
            'system_id'
        )

    def render_name(self, record, value):
        return mark_safe(u'<a href="{0}" title="Current record details">{1}</a>'.format(
            reverse('montenegro:public-officials', args=[record.id]), escape(value)
        ))

    def render_reports(self, record, value):
        return len(value)

    def render_year(self, record, value):
        if value:
            return value[0].year
        return ""

    def render_type(self, record, value):
        if value:
            return value[0].official_type
        return ""

    def render_position(self, record, value):
        if value:
            return value[0].public_office
        return ""

    def render_link(self, record, value):
        return mark_safe(u'<a href="{0}">source</a>'.format(value))


class CompanyTable(VeritzaTable):

    members = tables.Column(accessor='companymember_set')
    procurements = tables.Column(accessor='biddercompany_set')

    class Meta:
        model = models.Company
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok',
            'mail_address', 'name',  'status', 'system_id'
        )

    def render_registration_number(self, record, value):
        return mark_safe(u'<a href="{0}" title="Current record details">{1}</a>'.format(
            reverse('montenegro:companies', args=[record.id]), escape(value)
        ))

    def render_members(self, record, value):
        return len(value.all())

    def render_procurements(self, record, value):
        return len(value.all())


class CompanyMemberTable(VeritzaTable):

    class Meta:
        model = models.CompanyMember
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok',
            'mail_address', 'name',  'status', 'system_id', 'company_registration_number'
        )
        sequence = ['id', 'first_name', 'last_name', 'company']

    def render_id(self, record, value):
        return mark_safe(u'<a href="{0}" title="Current record details">{1}</a>'.format(
            reverse('montenegro:company-members', args=[record.id]), escape(value)
        ))

    def render_company(self, record, value):
        return mark_safe(u'<a href="{0}" title="Company details">{1}</a>'.format(
            reverse('montenegro:companies', args=[record.company.id]), escape(value)
        ))


class FamilyMemberTable(VeritzaTable):

    year = tables.Column(accessor='public_official', verbose_name='Year')
    type = tables.Column(accessor='public_official', verbose_name='Official type')
    position = tables.Column(accessor='public_official', verbose_name='Official position')

    class Meta:
        model = models.FamilyMember
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok',
            'mail_address',  'status', 'system_id'
        )

        sequence = ['name', 'public_official', 'relationship']

    def render_name(self, record, value):
        return mark_safe(u'<a href="{0}" title="Current record details">{1}</a>'.format(
            reverse('montenegro:family-members', args=[record.id]), escape(value)
        ))

    def render_public_official(self, record, value):
        return mark_safe(u'<a href="{0}" title="Official details">{1}</a>'.format(
            reverse('montenegro:public-officials', args=[record.public_official.id]), escape(value)
        ))

    def render_year(self, record, value):
        if value.publicofficialreport_set.all():
            return value.publicofficialreport_set.all()[0].year
        return ""

    def render_type(self, record, value):
        if value.publicofficialreport_set.all():
            return value.publicofficialreport_set.all()[0].official_type
        return ""

    def render_position(self, record, value):
        if value.publicofficialreport_set.all():
            return value.publicofficialreport_set.all()[0].public_office
        return ""


class PublicProcurementTable(VeritzaTable):
    winner = tables.Column(accessor='link', verbose_name='Winner')

    class Meta:
        model = models.PublicProcurement
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok',
            'system_id', 'record_type'
        )

    def render_number(self, record, value):
        return mark_safe(u'<a href="{0}" title="Current record details">{1}</a>'.format(
            reverse('montenegro:public-procurements', args=[record.id]), escape(value)
        ))

    def render_value(self, record, value):
        return mark_safe(u'{0} &euro;'.format(value))

    def render_winner(self, record, value):
        if record.biddercompany_set.all():
            winner = record.biddercompany_set.all()[0].company
            return mark_safe(u'<a href="{0}">{1}</a>'.format(reverse('montenegro:companies', args=[winner.id]), winner.name))
        return ""


class BidderCompanyTable(VeritzaTable):

    class Meta:
        model = models.BidderCompany
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok'
        )

    def render_id(self, record, value):
        return mark_safe(u'<a href="{0}" title="Current record details">{1}</a>'.format(
            reverse('montenegro:bidder-companies', args=[record.id]), escape(value)
        ))

    def render_company(self, record, value):
        return mark_safe(u'<a href="{0}" title="Company details">{1}</a>'.format(
            reverse('montenegro:companies', args=[record.company.id]), escape(value)
        ))

    def render_procurement(self, record, value):
        return mark_safe(u'<a href="{0}" title="Procurement details">{1}</a>'.format(
            reverse('montenegro:public-procurements', args=[record.procurement.id]), escape(value)
        ))


class ElectionsContributionsTable(VeritzaTable):

    class Meta:
        model = models.ElectionsContributions
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok', 'csv_file'
        )

    def render_id(self, record, value):
        return mark_safe(u'<a href="{0}" title="Current record details">{1}</a>'.format(
            reverse('montenegro:elections-contributions', args=[record.id]), escape(value)
        ))

    def render_amount(self, record, value):
        return mark_safe(u'{0} &euro;'.format(value))


class PublicOfficialCompanyTable(VeritzaTable):

    class Meta:
        model = models.PublicOfficialCompany
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok'
        )

    def render_id(self, record, value):
        return mark_safe(u'<a href="{0}" title="Current record details">{1}</a>'.format(
            reverse('montenegro:public-official-companies', args=[record.id]), escape(value)
        ))

    def render_official(self, record, value):
        return mark_safe(u'<a href="{0}" title="Official details">{1}</a>'.format(
            reverse('montenegro:public-officials', args=[record.official.id]), escape(value)
        ))

    def render_company(self, record, value):
        return mark_safe(u'<a href="{0}" title="Company details">{1}</a>'.format(
            reverse('montenegro:companies', args=[record.company.id]), escape(value)
        ))


class ConflictInterestTable(VeritzaTable):

    class Meta:
        model = models.ConflictInterest
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok',
            'mail_address', 'name',  'status', 'system_id', 'link'
        )

    def render_id(self, record, value):
        return mark_safe(u'<a href="{0}" title="Current record details">{1}</a>'.format(
            reverse('montenegro:public-official-companies', args=[record.id]), escape(value)
        ))

    def render_official(self, record, value):
        return mark_safe(u'<a href="{0}" title="Official details">{1}</a>'.format(
            reverse('montenegro:public-officials', args=[record.official.id]), escape(value)
        ))

    def render_company(self, record, value):
        return mark_safe(u'<a href="{0}" title="Company details">{1}</a>'.format(
            reverse('montenegro:companies', args=[record.company.id]), escape(value)
        ))

    def render_public_procurement(self, record, value):
        return mark_safe(u'<a href="{0}" title="Procurement details">{1}</a>'.format(
            reverse('montenegro:public-procurements', args=[record.public_procurement.id]), escape(value)
        ))


class FamilyMemberCompanyTable(VeritzaTable):

    class Meta:
        model = models.FamilyMemberCompany
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok'
        )

    def render_id(self, record, value):
        return mark_safe(u'<a href="{0}" title="Current record details">{1}</a>'.format(
            reverse('montenegro:companies', args=[record.id]), escape(value)
        ))

    def render_member(self, record, value):
        return mark_safe(u'<a href="{0}" title="Family member details">{1}</a>'.format(
            reverse('montenegro:family-members', args=[record.member.id]), escape(value)
        ))

    def render_company(self, record, value):
        return mark_safe(u'<a href="{0}" title="Company details">{1}</a>'.format(
            reverse('montenegro:companies', args=[record.company.id]), escape(value)
        ))


class ConflictInterestFamilyMemberTable(VeritzaTable):

    class Meta:
        model = models.ConflictInterestFamilyMember
        attrs = {"class": "paleblue table table-striped table-bordered"}
        exclude = (
            'id', 'uuid', 'created_by', 'created', 'updated', 'active', 'is_ok'
        )

    def render_id(self, record, value):
        return mark_safe(u'<a href="{0}" title="Current record details">{1}</a>'.format(
            reverse('montenegro:public-official-companies', args=[record.id]), escape(value)
        ))

    def render_member(self, record, value):
        return mark_safe(u'<a href="{0}" title="Official details">{1}</a>'.format(
            reverse('montenegro:family-members', args=[record.member.id]), escape(value)
        ))

    def render_company(self, record, value):
        return mark_safe(u'<a href="{0}" title="Company details">{1}</a>'.format(
            reverse('montenegro:companies', args=[record.company.id]), escape(value)
        ))

    def render_public_procurement(self, record, value):
        return mark_safe(u'<a href="{0}" title="Procurement details">{1}</a>'.format(
            reverse('montenegro:public-procurements', args=[record.public_procurement.id]), escape(value)
        ))
