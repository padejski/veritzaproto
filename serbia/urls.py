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
    url(r'^companies/(?P<pk>\d+)/$', views.CompanyDetailView.as_view(), name='company'),
    url(r'^datasets/$', views.DatasetsView.as_view(), name='datasets'),
    url(r'^officials/$', views.OfficialsView.as_view(), name='officials'),
    url(r'^offcials/(?P<pk>\d+)/$', views.OffcialDetailView.as_view(), name='official')
]

# ============================================================================
# EOF
# ============================================================================
