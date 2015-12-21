"""
Module    : urls
Date      : May, 2015
Author(s) : Matt Gathu <mattgathu@gmail.com>
Desc      : Veritza montenegro urls patterns

"""

from django.conf.urls import url

from apps.core import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='index'),
    url(r'^datasets/$', views.DatasetsView.as_view(), name='datasets'),

    url(r'^datasets/public-officials/$', views.PublicOfficialsView.as_view(), name='public-officials'),
    url(r'^datasets/public-officials/(?P<pk>\d+)/$', views.PublicOfficialDetailsView.as_view(), name='public-officials'),

    url(r'^datasets/companies/$', views.CompaniesView.as_view(), name='companies'),
    url(r'^datasets/companies/(?P<pk>\d+)/$', views.CompanyDetailsView.as_view(), name='companies'),

    url(r'^datasets/company-members/$', views.CompanyMembersView.as_view(), name='company-members'),
    url(r'^datasets/company-members/(?P<pk>\d+)/$', views.CompanyMemberDetailsView.as_view(), name='company-members'),

    url(r'^datasets/family-members/$', views.FamilyMembersView.as_view(), name='family-members'),
    url(r'^datasets/family-members/(?P<pk>\d+)/$', views.FamilyMemberDetailsView.as_view(), name='family-members'),

    url(r'^datasets/public-procurements/$', views.PublicProcurementsView.as_view(), name='public-procurements'),
    url(r'^datasets/public-procurements/(?P<pk>\d+)/$', views.PublicProcurementDetailsView.as_view(), name='public-procurements'),

    url(r'^datasets/bidder-companies/$', views.BidderCompaniesView.as_view(), name='bidder-companies'),
    url(r'^datasets/bidder-companies/(?P<pk>\d+)/$', views.BidderCompanyDetailsView.as_view(), name='bidder-companies'),

    url(r'^datasets/elections-contributions/$', views.ElectionsContributionsView.as_view(), name='elections-contributions'),
    url(r'^datasets/elections-contributions/(?P<pk>\d+)/$', views.ElectionsContributionsDetailsView.as_view(), name='elections-contributions'),

    url(r'^datasets/public-official-companies/$', views.PublicOfficialCompaniesView.as_view(), name='public-official-companies'),
    url(r'^datasets/public-official-companies/(?P<pk>\d+)/$', views.PublicOfficialCompanyDetailsView.as_view(), name='public-official-companies'),

    url(r'^datasets/conflict-interests/$', views.ConflictInterestsView.as_view(), name='conflict-interests'),
    url(r'^datasets/conflict-interests/(?P<pk>\d+)/$', views.ConflictInterestDetailsView.as_view(), name='conflict-interests'),

    url(r'^datasets/family-member-companies/$', views.FamilyMemberCompaniesView.as_view(), name='family-member-companies'),
    url(r'^datasets/family-member-companies/(?P<pk>\d+)/$', views.FamilyMemberCompanyDetailsView.as_view(), name='family-member-companies'),

    url(r'^datasets/conflict-interest-family-members/$', views.ConflictInterestFamilyMembersView.as_view(), name='conflict-interest-family-members'),
    url(r'^datasets/conflict-interest-family-members/(?P<pk>\d+)/$', views.ConflictInterestFamilyMemberDetailsView.as_view(), name='conflict-interest-family-members'),


]
