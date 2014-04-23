from django.conf.urls import patterns, include, url

from veritza.apps.core import views as core_views

urlpatterns = patterns(
    url(r'^datasets/', core_views.DatasetsView.as_view(), name='datasets'),
)