"""
views

"""
from django.views.generic import TemplateView
from django_tables2 import SingleTableView

from . import models, tables


class CompaniesView(SingleTableView):
    """list of companies view"""
    model = models.FedCompany
    table_class = tables.CompanyTable
    template_name = 'usa_companies.html'


class DatasetsView(TemplateView):
    """Datasets index view """
    template_name = 'usa_datasets.html'

    def get_context_data(self, **kwargs):
        context = super(DatasetsView, self).get_context_data(**kwargs)
        context['companies_no'] = models.FedCompany.objects.count()
        context['officials_no'] = 0

        return context


class IndexView(TemplateView):
    """Index view """
    template_name = 'usa_home.html'


class ProcurementsView(SingleTableView):
    """List of procurements """
    model = models.FedProcurement
    table_class = tables.ProcurementTable
    template_name = 'usa_procurements.html'
# ============================================================================
# EOF
# ============================================================================
