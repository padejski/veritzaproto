from django.views.generic import TemplateView
from django_tables2 import SingleTableView

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

	def get_queryset(self):
		return self.model.objects.select_related().all()

class PublicOfficialsView(DatasetView):
	model = PublicOfficial
	table_class = PublicOfficialTable


class CompaniesView(DatasetView):
	model = Company
	table_class = CompanyTable


class CompanyMembersView(DatasetView):
	model = CompanyMember
	table_class = CompanyMemberTable

	def get_queryset(self):
		# 'company' field needs to be explicitly requested here as
		# it is null=True and not select_related by default
		return self.model.objects.select_related('company').all()


class FamilyMembersView(DatasetView):
	model = FamilyMember
	table_class = FamilyMemberTable


class PublicProcurementsView(DatasetView):
	model = PublicProcurement
	table_class = PublicProcurementTable


class BidderCompaniesView(DatasetView):
	model = BidderCompany
	table_class = BidderCompanyTable


class ElectionsContributionsView(DatasetView):
	model = ElectionsContributions
	table_class = ElectionsContributionsTable


class PublicOfficialCompaniesView(DatasetView):
	model = PublicOfficialCompany
	table_class = PublicOfficialCompanyTable


class ConflictInterestsView(DatasetView):
	model = ConflictInterest
	table_class = ConflictInterestTable


class FamilyMemberCompaniesView(DatasetView):
	model = FamilyMemberCompany
	table_class = FamilyMemberCompanyTable


class ConflictInterestFamilyMembersView(DatasetView):
	model = ConflictInterestFamilyMember
	table_class = ConflictInterestFamilyMemberTable
