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
    url(r'^companies/$', views.CompaniesView.as_view(), name='companies'),
    url(r'^datasets/$', views.DatasetsView.as_view(), name='datasets'),
    url(r'^procurements/$', views.ProcurementsView.as_view(), name='procurements'),
    url(r'^electioncontribs/$', views.ElectionContributionsView.as_view(), name='econtribs'),
    url(r'^irsexempt/$', views.IrsExemptOrgsView.as_view(), name='irsexempts'),
    url(r'^secfilings/$', views.SecFilingsView.as_view(), name='secfilings'),
    url(r'^toxicsfacilities/$', views.ToxicsFacilitiesView.as_view(), name='toxicsfacilities'),
    url(r'^oshaebsa/$', views.OshaEbsasView.as_view(), name='oshaebsas'),
    url(r'^oshainsp/$', views.OshaInspectionsView.as_view(), name='oshainsps'),
    url(r'^cpscrecalls/$', views.CpscRecallsView.as_view(), name='cpscrecalls'),
    url(r'^cpscviols/$', views.CpscRecallViolationsView.as_view(), name='cpscviols'),
    url(r'^disclosures/$', views.FinancialDisclosuresView.as_view(), name='disclosures'),
    url(r'^candidates/$', views.CandidatesView.as_view(), name='candidates'),

    url(r'^companies/(?P<pk>\d+)/$', views.CompanyDetailView.as_view(), name='company'),
    url(r'^procurements/(?P<pk>\d+)/$', views.ProcurementDetailView.as_view(), name='procurement'),
    url(r'^electioncontribs/(?P<pk>\d+)/$', views.ElectionContributionDetailView.as_view(), name='econtrib'),
    url(r'^irsexempt/(?P<pk>\d+)/$', views.IrsExemptOrgDetailView.as_view(), name='irsexempt'),
    url(r'^secfilings/(?P<pk>\d+)/$', views.SecFilingDetailView.as_view(), name='secfiling'),
    url(r'^toxicsfacilities/(?P<pk>\d+)/$', views.ToxicsFacilityDetailView.as_view(), name='toxicsfacility'),
    url(r'^oshaebsa/(?P<pk>\d+)/$', views.OshaEbsaDetailView.as_view(), name='oshaebsa'),
    url(r'^oshainsp/(?P<pk>\d+)/$', views.OshaInspectionDetailView.as_view(), name='oshainsp'),
    url(r'^cpscrecalls/(?P<pk>\d+)/$', views.CpscRecallDetailView.as_view(), name='cpscrecall'),
    url(r'^cpscviols/(?P<pk>\d+)/$', views.CpscRecallViolationDetailView.as_view(), name='cpscviol'),
    url(r'^disclosures/(?P<pk>\d+)/$', views.FinancialDisclosureDetailView.as_view(), name='disclosure'),
    url(r'^candidates/(?P<pk>\d+)/$', views.CandidateDetailView.as_view(), name='candidate')

]

# ============================================================================
# EOF
# ============================================================================
