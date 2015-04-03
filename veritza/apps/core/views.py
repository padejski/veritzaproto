from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.shortcuts import render

from django_tables2 import SingleTableView
from report_tools.views import ReportView

from veritza.apps.core.reports import *
from veritza.apps.core.models import *
from veritza.apps.core.tables import *


class HomeView(TemplateView):
    template_name = 'home.html'


class DatasetsView(TemplateView):
    template_name = 'datasets.html'


class FaqView(TemplateView):
    template_name = 'faq.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class DatasetView(SingleTableView):
    template_name = 'core/list.html'
    stats_template = 'core/stats/empty.html'
    report = None

    def get_queryset(self):
        return self.model.objects.select_related().all()

    def get_context_data(self, **kwargs):
        context = super(DatasetView, self).get_context_data(**kwargs)
        context['stats_template'] = self.stats_template
        if self.report:
            context['report'] = self.report
        return context


class PublicOfficialsView(DatasetView, ReportView):
    model = PublicOfficial
    table_class = PublicOfficialTable
    stats_template = 'core/stats/public_officials.html'
    report = PublicOfficialsReport()

    def get_queryset(self):
        return self.model.objects.prefetch_related('publicofficialreport_set').all()


class PublicOfficialDetailsView(DetailView):
    model = PublicOfficial
    template_name = 'core/details/public_official.html'

    def get_object(self, **kwargs):
        obj = super(PublicOfficialDetailsView, self).get_object(**kwargs)
        obj.reports = PublicOfficialReport.objects.filter(official_id=obj.id)
        obj.official_companies = PublicOfficialCompany.objects.select_related('company').filter(official_id=obj.id)
        return obj


class CompaniesView(DatasetView):
    model = Company
    table_class = CompanyTable
    stats_template = 'core/stats/companies.html'
    report = CompaniesReport()

    def get_queryset(self):
        return self.model.objects.prefetch_related('companymember_set', 'biddercompany_set').all()


class CompanyDetailsView(DetailView):
    model = Company
    template_name = 'core/details/company.html'

    def get_object(self, **kwargs):
        obj = super(self.__class__, self).get_object(**kwargs)
        obj.company_members = CompanyMemberTitle.objects.select_related('company_member').filter(company_registration_number=obj.registration_number)
        obj.company_procurements = [bidder_company.procurement for bidder_company in BidderCompany.objects.select_related().filter(company_id=obj.id)]
        return obj


class CompanyMembersView(DatasetView):
    model = CompanyMember
    table_class = CompanyMemberTable

    def get_queryset(self):
        # 'company' field needs to be explicitly requested here as
        # it is null=True and not select_related by default
        return self.model.objects.select_related('company').all()


class CompanyMemberDetailsView(DetailView):
    model = CompanyMember
    template_name = 'core/details/company_member.html'

    def get_object(self, **kwargs):
        obj = super(self.__class__, self).get_object(**kwargs)
        obj.titles = CompanyMemberTitle.objects.filter(company_member_id=obj.id)
        return obj


class FamilyMembersView(DatasetView, ReportView):
    model = FamilyMember
    table_class = FamilyMemberTable
    stats_template = 'core/stats/family_members.html'
    report = FamilyMembersReport()


class FamilyMemberDetailsView(DetailView):
    model = FamilyMember


class PublicProcurementsView(DatasetView, ReportView):
    model = PublicProcurement
    table_class = PublicProcurementTable
    stats_template = 'core/stats/procurements.html'
    report = ProcurementsReport()


class PublicProcurementDetailsView(DatasetView):
    model = PublicProcurement


class BidderCompaniesView(DatasetView):
    model = BidderCompany
    table_class = BidderCompanyTable


class BidderCompanyDetailsView(DatasetView):
    model = BidderCompany


class ElectionsContributionsView(DatasetView, ReportView):
    model = ElectionsContributions
    table_class = ElectionsContributionsTable
    stats_template = 'core/stats/elections_contributions.html'
    report = ElectionsContributionsReport()

class ElectionsContributionsDetailsView(DatasetView):
    model = ElectionsContributions


class PublicOfficialCompaniesView(DatasetView):
    model = PublicOfficialCompany
    table_class = PublicOfficialCompanyTable


class PublicOfficialCompanyDetailsView(DatasetView):
    model = PublicOfficialCompany


class ConflictInterestsView(DatasetView):
    model = ConflictInterest
    table_class = ConflictInterestTable


class ConflictInterestDetailsView(DatasetView):
    model = ConflictInterest


class FamilyMemberCompaniesView(DatasetView):
    model = FamilyMemberCompany
    table_class = FamilyMemberCompanyTable


class FamilyMemberCompanyDetailsView(DatasetView):
    model = FamilyMemberCompany


class ConflictInterestFamilyMembersView(DatasetView):
    model = ConflictInterestFamilyMember
    table_class = ConflictInterestFamilyMemberTable


class ConflictInterestFamilyMemberDetailsView(DatasetView):
    model = ConflictInterestFamilyMember
