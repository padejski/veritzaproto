"""
Module    : urls
Date      : May, 2015
Author(s) : Matt Gathu <mattgathu@gmail.com>
Desc      : Veritza core urls patterns

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
    url(r'^$', views.IndexView.as_view(), name='home'),
    url(r'^datasets/$', views.DatasetsView.as_view(), name='datasets'),
    url(r'^faq/$', views.FaqView.as_view(), name='faq'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^scrapers/$', views.ScrapersView.as_view(), name='scrapers'),
    url(r'^subscription/$', views.SubscriptionView.as_view(), name='subscription'),
    url(r'^scrape/$', views.ScrapeView.as_view(), name='scrape'),
]

# ============================================================================
# EOF
# ============================================================================
