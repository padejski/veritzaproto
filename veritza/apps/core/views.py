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


class PublicOfficialsView(DatasetView):
	model = PublicOfficial
	table_class = PublicOfficialTable


class CompaniesView(DatasetView):
	model = Company
	table_class = CompanyTable


class ConflictInterestsView(DatasetView):
	model = ConflictInterest
	table_class = ConflictInterestTable
