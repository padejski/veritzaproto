from django.contrib import admin

from veritza.apps.core.models import (Dataset, Veritza, Person, PublicOfficialReport,
    Company, BidderCompany, ContractingAuthority, PublicProcurement, CompanyMember,
    ConflictInterest)  # , PublicOfficial)


class VeritzaAdminMixin(object):
    list_display = []


class VeritzaBaseAdmin(admin.ModelAdmin):
    pass


class DatasetAdmin(VeritzaBaseAdmin):
    list_display = ('name', 'source')


class VeritzaAdmin(VeritzaBaseAdmin):
    list_display = ('name',)


class PublicOfficialReportAdmin(VeritzaBaseAdmin):
    list_display = ('id', 'system_id', 'name', 'year', 'official_type', 'public_office', 'companies')
    search_fields = ('id', 'system_id', 'name', 'public_office', 'companies')


class CompanyAdmin(VeritzaBaseAdmin):
    list_display = ('id', 'registration_number', 'identification_number', 'full_name', 'address', 'status')
    search_fields = ('id', 'registration_number', 'identification_number', 'full_name', 'address', 'status')


class CompanyMemberAdmin(VeritzaBaseAdmin):
    list_display = ('id', 'company_registration_number', 'first_name', 'last_name', 'title')
    search_fields = ('id', 'company_registration_number', 'first_name', 'last_name', 'title')


class BidderCompanyAdmin(VeritzaBaseAdmin):
    list_display = ('id', 'identification_number', 'name', 'email', 'town')
    search_fields = ('id', 'identification_number', 'name', 'name')


class ContractingAuthorityAdmin(VeritzaBaseAdmin):
    list_display = ('id', 'name',)


class PublicProcurementAdmin(VeritzaBaseAdmin):
    list_display = ('id', 'number', 'title', 'record_type', 'description', 'creation_date', 'link')
    search_fields = ('id', 'number', 'record_type')
    list_filter = ('record_type',)


class ConflictInterestAdmin(VeritzaBaseAdmin):
    list_display = ('official', 'official_title', 'company_link', 'public_procurement_link')
    search_fields = ('official', 'company', 'public_procurement')
    readonly_fields = ('official', 'company', 'public_procurement')

    def company_link(self, obj):
        return u'<a href="{0}">{1}</a>'.format(obj.company.link, obj.company)
    company_link.allow_tags = True

    def public_procurement_link(self, obj):
        return u'<a href="{0}">{1}</a>'.format(obj.public_procurement.link, obj.public_procurement)
    public_procurement_link.allow_tags = True


admin.site.register(Dataset, DatasetAdmin)
admin.site.register(Veritza, VeritzaAdmin)
admin.site.register(Person)
# admin.site.register(PublicOfficial)
admin.site.register(PublicOfficialReport, PublicOfficialReportAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyMember, CompanyMemberAdmin)
admin.site.register(BidderCompany, BidderCompanyAdmin)
admin.site.register(ContractingAuthority, ContractingAuthorityAdmin)
admin.site.register(PublicProcurement, PublicProcurementAdmin)

admin.site.register(ConflictInterest, ConflictInterestAdmin)
