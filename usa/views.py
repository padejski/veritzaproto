"""
views

"""
from django.views.generic import TemplateView
from django_tables2 import SingleTableView

from . import models, tables


class CandidatesView(SingleTableView):
    """list of candidates view"""
    model = models.FedCandidate
    table_class = tables.CandidateTable
    template_name = 'usa_list.html'


class CompaniesView(SingleTableView):
    """list of companies view"""
    model = models.FedCompany
    table_class = tables.CompanyTable
    template_name = 'usa_list.html'

class CommitteeContributionsView(SingleTableView):
    """list of committee contributions"""
    model = models.FedCommitteeContribution
    table_class = tables.CommitteeContributionTable
    template_name = 'usa_list.html'




class DatasetsView(TemplateView):
    """Datasets index view """
    template_name = 'usa_datasets.html'

    def get_context_data(self, **kwargs):
        context = super(DatasetsView, self).get_context_data(**kwargs)
        context['companies_no'] = models.FedCompany.objects.count()
        context['disclosures_no'] = models.FedFinancialDisclosure.objects.count()
        context['procurements_no'] = models.FedProcurement.objects.count()
        context['irsexempt_no'] = models.FedIrsExemptOrg.objects.count()
        context['secfilings_no'] = models.FedSecFiling.objects.count()
        context['toxics_no'] = models.FedToxicsFacility.objects.count()
        context['oshaebsa_no'] = models.FedOshaEbsa.objects.count()
        context['oshainsp_no'] = models.FedOshaInspection.objects.count()
        context['cpscrecalls_no'] = models.FedCpscRecall.objects.count()
        context['cpscviol_no'] = models.FedCpscRecallViolation.objects.count()
        context['candidates_no'] = models.FedCandidate.objects.count()
        context['commcontribs_no'] = models.FedCommitteeContribution.objects.count()
        context['indvcontribs_no'] = models.FedIndividualContribution.objects.count()
        context['officials_no'] = 0

        return context

class FinancialDisclosuresView(SingleTableView):
    """list of Financial disclosures"""
    model = models.FedFinancialDisclosure
    table_class = tables.FinancialDisclosureTable
    template_name = 'usa_list.html'

class IndexView(TemplateView):
    """Index view """
    template_name = 'usa_home.html'


class IndividualContributionsView(SingleTableView):
    """list of Individual contributions"""
    model = models.FedIndividualContribution
    table_class = tables.IndividualContributionTable
    template_name = 'usa_list.html'


class IrsExemptOrgsView(SingleTableView):
    """list of IRS Exempt Organizations"""
    model = models.FedIrsExemptOrg
    table_class = tables.IrsExemptOrgTable
    template_name = 'usa_list.html'


class ProcurementsView(SingleTableView):
    """List of procurements """
    model = models.FedProcurement
    table_class = tables.ProcurementTable
    template_name = 'usa_list.html'


class SecFilingsView(SingleTableView):
    """list of SEC filings"""
    model = models.FedSecFiling
    table_class = tables.SecFilingTable
    template_name = 'usa_list.html'


class ToxicsFacilitiesView(SingleTableView):
    """list of Toxics facilities"""
    model = models.FedToxicsFacility
    table_class = tables.ToxicsFacilityTable
    template_name = 'usa_list.html'


class OshaEbsasView(SingleTableView):
    """list of OSHA EBSA"""
    model = models.FedOshaEbsa
    table_class = tables.OshaEbsaTable
    template_name = 'usa_list.html'


class OshaInspectionsView(SingleTableView):
    """list of OSHA inspections"""
    model = models.FedOshaInspection
    table_class = tables.OshaInspectionTable
    template_name = 'usa_list.html'


class CpscRecallsView(SingleTableView):
    """list of CPSC Recalls"""
    model = models.FedCpscRecall
    table_class = tables.CpscRecallTable
    template_name = 'usa_list.html'


class CpscRecallViolationsView(SingleTableView):
    """list of CPSC Recall Violations"""
    model = models.FedCpscRecallViolation
    table_class = tables.CpscRecallViolationTable
    template_name = 'usa_list.html'
# ============================================================================
# EOF
# ============================================================================
