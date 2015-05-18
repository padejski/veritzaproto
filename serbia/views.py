"""
Module    : views
Date      : May, 2015
Author(s) : Matt Gathu <mattgathu@gmail.com>
Desc      : Veritza serbia views


"""
# ============================================================================
# necessary imports
# ============================================================================
from django.views.generic import TemplateView, DetailView
# from django.shortcuts import get_object_or_404
from django_tables2 import SingleTableView

from . import models, tables


# ============================================================================
# class based views
# ============================================================================
class CompaniesView(SingleTableView):
    """list of companies view"""
    model = models.Company
    table_class = tables.CompanyTable
    template_name = 'serbia_companies.html'


class CompanyDetailView(DetailView):

    model = models.Company
    template_name = 'serbia_company.html'


class DatasetsView(TemplateView):
    template_name = 'serbia_datasets.html'

    def get_context_data(self, **kwargs):
        context = super(DatasetsView, self).get_context_data(**kwargs)
        context['officials_no'] = models.Official.objects.count()
        context['companies_no'] = models.Company.objects.count()

        return context


class IndexView(TemplateView):
    template_name = 'serbia_home.html'


class OfficialsView(SingleTableView):
    """list of public officials view"""
    model = models.Official
    table_class = tables.OfficialTable
    template_name = 'serbia_officials.html'


class OffcialDetailView(DetailView):
    model = models.Official
    template_name = 'serbia_official.html'
# ============================================================================
# EOF
# ============================================================================
