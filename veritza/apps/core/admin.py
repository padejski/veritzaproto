# -*- coding: utf-8 -*-
import logging

from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter
from django.contrib import admin

from veritza.apps.core.models import (
    Dataset, Veritza, Person, PublicOfficial, PublicOfficialReport,
    Company, ProcurementCompany, ProcurementCompanyRaw, BidderCompany, ContractingAuthority, PublicProcurement, CompanyMember,
    ConflictInterest, PublicOfficialCompany, ElectionsContributions
)

logger = logging.getLogger('debug')


class ProcurementValueListFilter(SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Value range')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'value'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('1 - 1000', _(u'1 - 1 000 €')),
            ('1000 - 5000', _(u'1 000 - 5 000 €')),
            ('5000 - 10000', _(u'5 000 - 10 000 €')),
            ('10000 - 20000', _(u'10 000 - 20 000 €')),
            ('20000 - 30000', _(u'20 000 - 30 000 €')),
            ('30000 - 40000', _(u'30 000 - 40 000 €')),
            ('40000 - 50000', _(u'40 000 - 50 000 €')),
            ('50000 - 100000', _(u'50 000 - 100 000 €')),
            ('100000 - 500000', _(u'100 000 - 500 000 €')),
            ('500000 - 1000000', _(u'500 000 - 1 000 000 €')),
            ('1000000 - ', _(u'1 000 000 + €')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value
        # to decide how to filter the queryset.
        if self.value():
            start, end = self.value().split(' - ')
            if end:
                return queryset.filter(value__gte=int(start),
                                       value__lte=int(end))
            elif not end:
                return queryset.filter(value__gte=int(start))
        return None


class VeritzaAdminMixin(object):
    list_display = []


class VeritzaBaseAdmin(admin.ModelAdmin):
    pass


class DatasetAdmin(VeritzaBaseAdmin):
    list_display = ('name', 'source')


class VeritzaAdmin(VeritzaBaseAdmin):
    list_display = ('name',)


# MIXINS ############################################
class CompanyLinkAdminMixin(object):
    def company_link(self, obj):
        return u'<a href="/admin/core/company/{0}">{1}</a> - [<a href="{2}">source</a>]'.format(obj.company.id, obj.company, obj.company.link)
    company_link.allow_tags = True
    company_link.short_description = "Company"


class OfficialLinkAdminMixin(object):
    def official_link(self, obj):
        return u'<a href="/admin/core/official/{0}">{1}</a> - [<a href="{2}">source</a>]'.format(obj.official.id, obj.official.name, obj.official.link)
    official_link.allow_tags = True
    official_link.short_description = "Official"


class ProcurementLinkAdminMixin(object):
    def public_procurement_link(self, obj):
        return u'<a href="/admin/core/publicprocurement/{0}">{1}</a> - [<a href="{2}">source</a>]'.format(obj.public_procurement.id, obj.public_procurement, obj.public_procurement.link)
    public_procurement_link.allow_tags = True
    public_procurement_link.short_description = "Procurement"
# END MIXINS ############################################


# INLINES ############################################
class ConflictInterestInline(admin.TabularInline, OfficialLinkAdminMixin, CompanyLinkAdminMixin, ProcurementLinkAdminMixin):
    model = ConflictInterest
    verbose_name = "Alerts"
    extra = 0
    fields = ('official_link', 'company_link', 'public_procurement_link')
    readonly_fields = ('official_link', 'company_link', 'public_procurement_link')


class OfficialAlertInline(admin.TabularInline, OfficialLinkAdminMixin, CompanyLinkAdminMixin):
    model = ConflictInterest
    verbose_name = "Alerts"
    extra = 0
    fields = ('company_link', 'public_procurement_link')
    readonly_fields = ('official_link', 'company_link', 'public_procurement_link')

    def public_procurement_link(self, obj):
        return u'<a href="/admin/core/publicprocurement/{0}">{1}</a> - [<a href="{2}">source</a>]'.format(obj.public_procurement.id, obj.public_procurement, obj.public_procurement.link)
    public_procurement_link.allow_tags = True
    public_procurement_link.short_description = "Procurement"


class CompanyAlertInline(admin.TabularInline, OfficialLinkAdminMixin, CompanyLinkAdminMixin):
    model = ConflictInterest
    verbose_name = "Alerts"
    extra = 0
    fields = ('official_link', 'public_procurement_link')
    readonly_fields = ('official_link', 'public_procurement_link')

    def public_procurement_link(self, obj):
        return u'<a href="/admin/core/publicprocurement/{0}">{1}</a> - [<a href="{2}">source</a>]'.format(obj.public_procurement.id, obj.public_procurement, obj.public_procurement.link)
    public_procurement_link.allow_tags = True
    public_procurement_link.short_description = "Procurement"


class ProcurementAlertInline(admin.TabularInline, OfficialLinkAdminMixin, CompanyLinkAdminMixin):
    model = ConflictInterest
    verbose_name = "Alerts"
    extra = 0
    fields = ('official_link', 'company_link')
    readonly_fields = ('official_link', 'company_link',)


class PublicOfficialReportInline(admin.TabularInline, OfficialLinkAdminMixin):
    model = PublicOfficialReport

    extra = 0
    fields = ('official_link', 'report_name_link', 'year', 'official_type', 'public_office')
    readonly_fields = ('official_link', 'report_name_link',)

    def report_name_link(self, obj):
        return u'<a href="/admin/core/publicofficialreport/{0}">{1}</a>'.format(obj.id, obj.report_name)
    report_name_link.allow_tags = True


class PublicOfficialCompanyInline(admin.TabularInline, OfficialLinkAdminMixin, CompanyLinkAdminMixin):
    model = PublicOfficialCompany

    extra = 0
    readonly_fields = ['official', 'company']
    # fields = ['official_link', 'company_link']


class CompanyMemberInline(admin.TabularInline):
    model = CompanyMember
    fields = ('first_name_link', 'last_name_link', 'webpage')
    readonly_fields = fields + ('company_registration_number', 'created_by', )
    extra = 0

    def first_name_link(self, obj):
        return u'<a href="/admin/core/companymember/{0}">{1}</a>'.format(obj.id, obj.first_name)
    first_name_link.allow_tags = True
    first_name_link.short_description = "First Name"

    def last_name_link(self, obj):
        return u'<a href="/admin/core/companymember/{0}">{1}</a>'.format(obj.id, obj.last_name)
    last_name_link.allow_tags = True
    last_name_link.short_description = "Last Name"

    def webpage(self, obj):
        return u'<a href="{0}">{0}</a>'.format(obj.link) if obj.link else " - "
    webpage.allow_tags = True
# END INLINES ############################################


class ConflictInterestAdmin(VeritzaBaseAdmin, OfficialLinkAdminMixin, CompanyLinkAdminMixin):
    list_display = ('official', 'official_title', 'company_link', 'public_procurement_link')
    search_fields = ('official__name', 'company__full_name',)
    fields = ('official_link', 'company_link', 'public_procurement_link')
    readonly_fields = ('official', 'official_link', 'company', 'company_link', 'public_procurement', 'public_procurement_link')
    # list_filter = ('official_title',)

    verbose_name = "Alert"

    def official_link(self, obj):
        return u'<a href="/admin/core/publicofficial/{0}">{1}</a> - [source]'.format(obj.official.id, obj.official.name)
    official_link.allow_tags = True
    official_link.short_description = "Official"

    def company_link(self, obj):
        return u'<a href="/admin/core/company/{0}">{1}</a> - [<a href="{2}">source</a>]'.format(obj.company.id, obj.company, obj.company.link)
    company_link.allow_tags = True
    company_link.short_description = "Company"

    def public_procurement_link(self, obj):
        return u'<a href="/admin/core/publicprocurement/{0}">{1}</a> - [<a href="{2}">source</a>]'.format(obj.public_procurement.id, obj.public_procurement, obj.public_procurement.link)
    public_procurement_link.allow_tags = True
    public_procurement_link.short_description = "Procurement"


class ElectionsContributionsAdmin(VeritzaBaseAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(ElectionsContributionsAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['created_by'].initial = request.user.id
        # form.base_fields['created_by'].widget = request.user.id
        return form

    fieldsets = (
        ('File upload',
            {'fields': ['csv_file']}),
        ('Manual data entry',
            {'fields': ['date', 'election_type', 'election_place', 'political_party',
                        'candidate', 'contributor_type', 'contributor_name',
                        'contributor_address', 'amount', 'created_by']})
    )


class PublicOfficialReportAdmin(VeritzaBaseAdmin, OfficialLinkAdminMixin):
    list_display = ('id', 'system_id', 'name', 'year', 'official_type', 'salary',
                    'public_office', 'companies', 'report_type', 'rbr', 'address', 'job',
                    'spouse', 'webpage')
    search_fields = ('id', 'system_id', 'name', 'public_office', 'companies')
    list_filter = ('official_type', 'year', 'public_office', 'report_type')
    readonly_fields = ('system_id', 'official_link',)

    def webpage(self, obj):
        return u'<a href="{0}">{0}</a>'.format(obj.link) if obj.link else " - "
    webpage.allow_tags = True

    def public_official_link(self, obj):
        return u'<a href="/admin/core/publicofficial/{0}">{1}</a>'.format(obj.official.id, obj.official.name)
    public_official_link.allow_tags = True

    fieldsets = (
        ('Personal information', {
            'fields': (('official_link', 'name', 'system_id'),)
        }),
        ('Office information', {
            'fields': ('official_type', ('public_office', 'public_office_other',))
        }),
        ('Report information', {
            'fields': (('report_name', 'report_type'), ('year', 'rbr'), 'link')
        }),
        ('Public official information', {
            'fields': (
                'job', 'address',
                ('company_board_member', 'salary'),
                ('other_activities', 'other_activities_salary'),
                'real_estate',
                ('movables', 'movables_others'),
                ('companies', 'company_salary'),
                'annual_income', 'other_income', 'credits_debts'
            )
        }),
        ('Spouse information', {
            'fields': (
                'spouse',
                ('spouse_job', 'spouse_other_activities',),
                'spouse_real_estate',
                ('spouse_movables', 'spouse_movables_others'),
                ('spouse_companies', 'spouse_company_salary'),
                'spouse_annual_income', 'spouse_other_income', 'spouse_credits_debts'
            )
        }),
    )


class PublicOfficialCompanyAdmin(VeritzaBaseAdmin):
    list_display = ('official_link', 'company_link')
    readonly_fields = ('official', 'company', 'official_link', 'company_link')
    fields = ('official_link', 'company_link')

    def official_link(self, obj):
        return u'<a href="/admin/core/publicofficial/{0}">{1}</a>'.format(obj.official_id, obj.official.name)
    official_link.allow_tags = True
    official_link.short_description = "Official"

    def company_link(self, obj):
        return u'<a href="/admin/core/company/{0}">{1}</a>'.format(obj.company_id, obj.company.full_name)
    company_link.short_description = "Company"
    company_link.allow_tags = True


class PublicOfficialAdmin(OfficialLinkAdminMixin, VeritzaBaseAdmin):
    list_display = ('name', 'alerts', 'companies', 'system_id',)
    readonly_fields = ('official_link',)
    search_fields = ('name',)
    fieldsets = (
        ('Personal information', {
            'fields': ('official_link', 'system_id',),
        }),
    )

    def official_link(self, obj):
        return u'<a href="/admin/core/official/{0}">{1}</a> - [<a href="{2}">source</a>]'.format(obj.id, obj.name, obj.link)
    official_link.allow_tags = True
    official_link.short_description = "Official"

    inlines = [
        OfficialAlertInline,
        PublicOfficialCompanyInline,
        PublicOfficialReportInline,
    ]

    def alerts(self, obj):
        return obj.conflictinterest_set.count()

    def companies(self, obj):
        return obj.publicofficialcompany_set.count()


class CompanyAdmin(VeritzaBaseAdmin):
    list_display = ('id', 'registration_number', 'identification_number', 'full_name', 'members',
                    'alerts', 'officials_members', 'economic_activity', 'activity', 'address',
                    'registration_date', 'status', 'webpage',)
    list_display_links = ('id', 'registration_number',)
    search_fields = ('id', 'registration_number', 'identification_number', 'full_name', 'address')
    list_filter = ('status', 'registration_date', 'economic_activity', 'location')
    readonly_fields = ('full_name',)

    inlines = [
        CompanyAlertInline,
        CompanyMemberInline,
        PublicOfficialCompanyInline,
    ]

    def members(self, obj):
        return obj.companymember_set.count()

    def alerts(self, obj):
        return obj.conflictinterest_set.count()

    def officials_members(self, obj):
        return obj.publicofficialcompany_set.count()

    def webpage(self, obj):
        return u'<a href="{0}">{0}</a>'.format(obj.link) if obj.link else " - "
    webpage.allow_tags = True


class CompanyMemberAdmin(VeritzaBaseAdmin):
    list_display = ('id', 'company_registration_number', 'first_name', 'last_name',)
    search_fields = ('id', 'company_registration_number', 'first_name', 'last_name')
    readonly_fields = ('company',)


class BidderCompanyAdmin(CompanyLinkAdminMixin, ProcurementLinkAdminMixin, VeritzaBaseAdmin):
    readonly_fields = ('company', 'procurement', 'company_link', 'public_procurement_link')
    fields = ('company_link', 'public_procurement_link')

    def public_procurement_link(self, obj):
        return u'<a href="/admin/core/publicprocurement/{0}">{1}</a> - [<a href="{2}">source</a>]'.format(obj.procurement.id, obj.procurement, obj.procurement.link)
    public_procurement_link.allow_tags = True
    public_procurement_link.short_description = "Procurement"



class ProcurementCompanyAdmin(VeritzaBaseAdmin):
    list_display = ('id', 'identification_number', 'name', 'postal_address', 'contact_point',
                    'email', 'town', 'public_procurement', 'link')
    search_fields = ('id', 'identification_number', 'name', 'name')

    def link(self, obj):
        if obj.webpage.strip() and obj.webpage.strip() != 'nema' and len(obj.webpage.strip()) > 10:
            return u'<a href="{0}">{0}</a>'.format(obj.webpage)
        return u'-'
    link.allow_tags = True

    def public_procurement(self, obj):
        try:
            procurement = PublicProcurement.objects.filter(number=obj.procurement_number, system_id=obj.procurement_system_id)
            if procurement:
                procurement = procurement[0]
                return u"<a href='http://portal.ujn.gov.me/delta/search/displayNotice.html?id={0}'>{1}<br/># <strong>{2}</strong></a>".format(procurement.system_id, procurement.title, procurement.number)
            else:
                return "-"
        except Exception as e:
            logger.exception(e)
            return u"<a href='http://portal.ujn.gov.me/delta/search/displayNotice.html?id={0}'>{1}</a>".format(procurement.system_id, procurement.number)
    public_procurement.allow_tags = True


class ProcurementCompanyAdminRaw(ProcurementCompanyAdmin):
    pass


class ContractingAuthorityAdmin(VeritzaBaseAdmin):
    list_display = ('id', 'identification_number', 'name', 'address', 'town', 'email', 'link')

    def link(self, obj):
        return u'<a href="{0}">{0}</a>'.format(obj.webpage) if obj.webpage else " - "
    link.allow_tags = True


class PublicProcurementAdmin(VeritzaBaseAdmin):
    list_display = ('number', 'title', 'alerts', 'subject', 'authority', 'company',
                    'record_type', 'value_currency', 'creation_date', 'location', 'webpage')
    list_display_links = ('number',)
    search_fields = ('id', 'number', 'record_type')
    list_filter = ('record_type', 'subject', 'creation_date', ProcurementValueListFilter, 'location')

    inlines = [
        ProcurementAlertInline,
    ]

    def alerts(self, obj):
        return obj.conflictinterest_set.count()

    def webpage(self, obj):
        return u'<a href="{0}">{0}</a>'.format(obj.link)
    webpage.allow_tags = True

    def value_currency(self, obj):
        return u'{0} €'.format(obj.value)

    def company(self, obj):
        try:
            return BidderCompany.objects.get(procurement_number=obj.number).name
        except Exception:
            return "-"

    def authority(self, obj):
        try:
            return ContractingAuthority.objects.get(procurement_number=obj.number).name
        except Exception:
            return "-"


admin.site.register(Dataset, DatasetAdmin)
admin.site.register(Veritza, VeritzaAdmin)
admin.site.register(Person)
admin.site.register(ElectionsContributions, ElectionsContributionsAdmin)
admin.site.register(PublicOfficial, PublicOfficialAdmin)
admin.site.register(PublicOfficialReport, PublicOfficialReportAdmin)
admin.site.register(PublicOfficialCompany, PublicOfficialCompanyAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyMember, CompanyMemberAdmin)
admin.site.register(ProcurementCompany, ProcurementCompanyAdmin)
admin.site.register(ProcurementCompanyRaw, ProcurementCompanyAdminRaw)
admin.site.register(BidderCompany, BidderCompanyAdmin)
admin.site.register(ContractingAuthority, ContractingAuthorityAdmin)
admin.site.register(PublicProcurement, PublicProcurementAdmin)

admin.site.register(ConflictInterest, ConflictInterestAdmin)
