"""
Module    : urls
Date      : May, 2015
Author(s) : Matt Gathu <mattgathu@gmail.com>
Desc      : Veritza serbia urls patterns

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

    url(r'^companies/(?P<pk>\d+)/$', views.CompanyDetailView.as_view(),
        name='company'),
    url(r'^datasets/$', views.DatasetsView.as_view(), name='datasets'),

    url(r'^electioncontribs/$', views.ElectionDonationsView.as_view(),
        name='electioncontribs'),
    url(r'^electioncontribs/(?P<pk>\d+)/$',
        views.ElectionDonationDetailView.as_view(), name='electioncontrib'),
    url(r'^officials/$', views.OfficialsView.as_view(), name='officials'),

    url(r'^officials/(?P<pk>\d+)/$', views.OfficialDetailView.as_view(),
        name='official'),
    url(r'^procurements/$', views.ProcurementsView.as_view(),
        name='procurements'),
    url(r'^procurements/(?P<pk>\d+)/$', views.ProcurementDetailView.as_view(),
        name='procurement'),
    url(r'^officialscompanies/$', views.OfficialsCompanies.as_view(),
        name='officialscompanies'),
    url(r'^officialscompaniesprocurement/$',
        views.OfficialsCompaniesProcurement.as_view(), name='officialscompaniesprocurement'),
    url(r'^funderscompanies/$',
        views.FundersCompanies.as_view(), name='funderscompanies'),
    url(r'^funderscompaniesprocurement',
        views.FundersCompaniesProcurement.as_view(), name='funderscompaniesprocurement'),
    url(r'^fundingcompaniesprocurement',
        views.FundingCompaniesProcurement.as_view(), name='fundingcompaniesprocurement')
]

# ============================================================================
# EOF
# ============================================================================
