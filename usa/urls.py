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
    url(r'^indvcontribs/$', views.IndividualContributionsView.as_view(), name='indvcontribs'),
    url(r'^commcontribs/$', views.CommitteeContributionsView.as_view(), name='commcontribs'),
    url(r'^irsexempt/$', views.IrsExemptOrgsView.as_view(), name='irsexempt'),
    url(r'^secfilings/$', views.SecFilingsView.as_view(), name='secfilings'),
    url(r'^toxicsfacilities/$', views.ToxicsFacilitiesView.as_view(), name='toxicsfacilities'),
    url(r'^oshaebsa/$', views.OshaEbsasView.as_view(), name='oshaebsa'),
    url(r'^oshainsp/$', views.OshaInspectionsView.as_view(), name='oshainsp'),
    url(r'^cpscrecalls/$', views.CpscRecallsView.as_view(), name='cpscrecalls'),
    url(r'^cpscviols/$', views.CpscRecallViolationsView.as_view(), name='cpscviols'),
    url(r'^disclosures/$', views.FinancialDisclosuresView.as_view(), name='disclosures'),
    url(r'^candidates/$', views.CandidatesView.as_view(), name='candidates')
]

# ============================================================================
# EOF
# ============================================================================
