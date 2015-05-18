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
    url(r'^procurements/$', views.ProcurementsView.as_view(), name='procurements')
]

# ============================================================================
# EOF
# ============================================================================
