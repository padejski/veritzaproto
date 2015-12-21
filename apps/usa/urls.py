"""
Module    : urls
Date      : May, 2015
Author(s) : Matt Gathu <mattgathu@gmail.com>
Desc      : Veritza usa urls patterns

"""
# ============================================================================
# necessary imports
# ============================================================================
from django.conf.urls import url

from . import views

# ============================================================================
# url patterns
# ============================================================================
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^companies/$', views.CompaniesView.as_view(), name='federal-companies'),
    url(r'^datasets/$', views.DatasetsView.as_view(), name='datasets'),
    url(r'^procurements/$', views.ProcurementsView.as_view(), name='federal-procurement'),
    url(r'^electioncontribs/$', views.ElectionContributionsView.as_view(), name='elections-contributions'),
    url(r'^irsexempt/$', views.IrsExemptOrgsView.as_view(), name='irs-exempt-organizations'),
    url(r'^secfilings/$', views.SecFilingsView.as_view(), name='securities-and-exchange-commission-filings'),
    url(r'^toxicsfacilities/$', views.ToxicsFacilitiesView.as_view(), name='toxics-facilities'),
    url(r'^oshaebsa/$', views.OshaEbsasView.as_view(), name='osha-employee-benefits-security-adminstration-enforcements'),
    url(r'^oshainsp/$', views.OshaInspectionsView.as_view(), name='occupational-safety-and-health-inspections'),
    url(r'^cpscrecalls/$', views.CpscRecallsView.as_view(), name='consumer-product-safety-commission-recalls'),
    url(r'^cpscviols/$', views.CpscRecallViolationsView.as_view(), name='consumer-product-safety-commission-recall-violations'),
    url(r'^disclosures/$', views.FinancialDisclosuresView.as_view(), name='federal-financial-disclosures'),
    url(r'^candidates/$', views.CandidatesView.as_view(), name='election-candidates'),

    url(r'^companies/(?P<pk>\d+)/$', views.CompanyDetailView.as_view(), name='federal-companies'),
    url(r'^procurements/(?P<pk>\d+)/$', views.ProcurementDetailView.as_view(), name='federal-procurement'),
    url(r'^electioncontribs/(?P<pk>\d+)/$', views.ElectionContributionDetailView.as_view(), name='elections-contributions'),
    url(r'^irsexempt/(?P<pk>\d+)/$', views.IrsExemptOrgDetailView.as_view(), name='irs-exempt-organizations'),
    url(r'^secfilings/(?P<pk>\d+)/$', views.SecFilingDetailView.as_view(), name='securities-and-exchange-commission-filings'),
    url(r'^toxicsfacilities/(?P<pk>\d+)/$', views.ToxicsFacilityDetailView.as_view(), name='toxics-facilities'),
    url(r'^oshaebsa/(?P<pk>\d+)/$', views.OshaEbsaDetailView.as_view(), name='osha-employee-benefits-security-adminstration-enforcements'),
    url(r'^oshainsp/(?P<pk>\d+)/$', views.OshaInspectionDetailView.as_view(), name='occupational-safety-and-health-inspections'),
    url(r'^cpscrecalls/(?P<pk>\d+)/$', views.CpscRecallDetailView.as_view(), name='consumer-product-safety-commission-recalls'),
    url(r'^cpscviols/(?P<pk>\d+)/$', views.CpscRecallViolationDetailView.as_view(), name='consumer-product-safety-commission-recall-violations'),
    url(r'^disclosures/(?P<pk>\d+)/$', views.FinancialDisclosureDetailView.as_view(), name='federal-financial-disclosures'),
    url(r'^candidates/(?P<pk>\d+)/$', views.CandidateDetailView.as_view(), name='election-candidates'),

    url(r'^search', views.SearchView.as_view(), name='search'),

]

# ============================================================================
# EOF
# ============================================================================
