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
from django_tables2 import SingleTableView

from . import models, tables


# ============================================================================
# class based views
# ============================================================================
class CompaniesView(SingleTableView):
    """list of companies view"""
    model = models.Company
    table_class = tables.CompanyTable
    template_name = 'serbia_list.html'


class CompanyDetailView(DetailView):

    model = models.Company
    template_name = 'serbia_company.html'


class DatasetsView(TemplateView):
    template_name = 'serbia_datasets.html'

    def get_context_data(self, **kwargs):
        context = super(DatasetsView, self).get_context_data(**kwargs)
        context['officials_no'] = models.Official.objects.count()
        context['companies_no'] = models.Company.objects.count()
        context['procurements_no'] = models.Procurement.objects.count()
        context['edonations_no'] = models.ElectionDonation.objects.count()
        context['offcompanies_no'] = models.OfficialCompany.objects.count()
        context['offcompaniesproc_no'] = models.OfficialCompanyProcurement.objects.count()
        context['funderscompanies_no'] = models.FunderCompany.objects.count()
        context['funderscompaniesproc_no'] = models.FunderCompanyProcurement.objects.count()
        context['fundingcompaniesproc_no'] = models.FundingCompanyProcurement.objects.count()

        return context


class ElectionDonationsView(SingleTableView):
    """list of election donations"""
    model = models.ElectionDonation
    table_class = tables.ElectionDonationTable
    template_name = 'serbia_list.html'


class ElectionDonationDetailView(DetailView):
    model = models.ElectionDonation
    template_name = 'serbia_election_donation.html'


class IndexView(TemplateView):
    template_name = 'serbia_home.html'


class OfficialsView(SingleTableView):
    """list of public officials view"""
    model = models.Official
    table_class = tables.OfficialTable
    template_name = 'serbia_list.html'


class OfficialDetailView(DetailView):
    model = models.Official
    template_name = 'serbia_official.html'


class ProcurementsView(SingleTableView):
    """list of procurement view"""
    model = models.Procurement
    table_class = tables.ProcurementTable
    template_name = 'serbia_list.html'


class ProcurementDetailView(DetailView):
    model = models.Procurement
    template_name = 'serbia_procurement.html'


class OfficialsCompanies(SingleTableView):
    """list of public officials' companies"""
    model = models.OfficialCompany
    table_class = tables.OfficialCompanyTable
    template_name = 'serbia_list.html'


class OfficialsCompaniesProcurement(SingleTableView):
    """list of public officials companies in procurement"""
    model = models.OfficialCompanyProcurement
    table_class = tables.OfficialCompanyProcurementTable
    template_name = 'serbia_list.html'


class FundersCompanies(SingleTableView):
    """list of election donors/funders companies"""
    model = models.FunderCompany
    table_class = tables.FunderCompanyTable
    template_name = 'serbia_list.html'


class FundersCompaniesProcurement(SingleTableView):
    """list of companies in procurement owned by political funders"""
    model = models.FunderCompanyProcurement
    table_class = tables.FunderCompanyProcurementTable
    template_name = 'serbia_list.html'


class FundingCompaniesProcurement(SingleTableView):
    """list of companies that are funders and also are in procurement"""
    model = models.FundingCompanyProcurement
    table_class = tables.FundingCompanyProcurementTable
    template_name = 'serbia_list.html'
# ============================================================================
# EOF
# ============================================================================
