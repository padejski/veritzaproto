from django.views.generic import TemplateView
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


class PublicOfficialsView(DatasetView):
    model = PublicOfficial
    table_class = PublicOfficialTable


class PublicOfficialDetailsView(TemplateView):
    model = PublicOfficial


class CompaniesView(DatasetView):
    model = Company
    table_class = CompanyTable
    stats_template = 'core/stats/companies.html'
    report = CompaniesReport()


class CompanyDetailsView(DatasetView):
    model = Company


class CompanyMembersView(DatasetView):
    model = CompanyMember
    table_class = CompanyMemberTable

    def get_queryset(self):
        # 'company' field needs to be explicitly requested here as
        # it is null=True and not select_related by default
        return self.model.objects.select_related('company').all()


class CompanyMemberDetailsView(DatasetView):
    model = CompanyMember


class FamilyMembersView(DatasetView):
    model = FamilyMember
    table_class = FamilyMemberTable
    stats_template = 'core/stats/family_members.html'
    report = FamilyMembersReport()


class FamilyMemberDetailsView(DatasetView, ReportView):
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
