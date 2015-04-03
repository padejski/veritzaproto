from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from veritza.apps.core import views as core_views

admin.autodiscover()

urlpatterns = patterns('',
    (r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('userena.urls')),

    url(r'^$', core_views.HomeView.as_view(), name='home'),
    url(r'^faq/', core_views.FaqView.as_view(), name='faq'),
    url(r'^about/', core_views.AboutView.as_view(), name='about'),
    url(r'^contact/', core_views.ContactView.as_view(), name='contact'),
    url(r'^datasets/$', core_views.DatasetsView.as_view(), name='datasets'),

    url(r'^datasets/public-officials/$', core_views.PublicOfficialsView.as_view(), name='public-officials'),
    url(r'^datasets/public-officials/(?P<pk>\d+)/$', core_views.PublicOfficialDetailsView.as_view(), name='public-official-details'),

    url(r'^datasets/companies/$', core_views.CompaniesView.as_view(), name='companies'),
    url(r'^datasets/companies/(?P<pk>\d+)/$', core_views.CompanyDetailsView.as_view(), name='company-details'),

    url(r'^datasets/company-members/$', core_views.CompanyMembersView.as_view(), name='company-members'),
    url(r'^datasets/company-members/(\d+)/$', core_views.CompanyMemberDetailsView.as_view(), name='company-member-details'),

    url(r'^datasets/family-members/$', core_views.FamilyMembersView.as_view(), name='family-members'),
    url(r'^datasets/family-members/(\d+)/$', core_views.FamilyMemberDetailsView.as_view(), name='family-member-details'),

    url(r'^datasets/public-procurements/$', core_views.PublicProcurementsView.as_view(), name='public-procurements'),
    url(r'^datasets/public-procurements/(\d+)/$', core_views.PublicProcurementDetailsView.as_view(), name='public-procurement-details'),

    url(r'^datasets/bidder-companies/$', core_views.BidderCompaniesView.as_view(), name='bidder-companies'),
    url(r'^datasets/bidder-companies/(\d+)/$', core_views.BidderCompanyDetailsView.as_view(), name='bidder-company-details'),

    url(r'^datasets/elections-contributions/$', core_views.ElectionsContributionsView.as_view(), name='elections-contributions'),
    url(r'^datasets/elections-contributions/(\d+)/$', core_views.ElectionsContributionsDetailsView.as_view(), name='elections-contributions-details'),

    url(r'^datasets/public-official-companies/$', core_views.PublicOfficialCompaniesView.as_view(), name='public-official-companies'),
    url(r'^datasets/public-official-companies/(\d+)/$', core_views.PublicOfficialCompanyDetailsView.as_view(), name='public-official-company-details'),

    url(r'^datasets/conflict-interests/$', core_views.ConflictInterestsView.as_view(), name='conflict-interests'),
    url(r'^datasets/conflict-interests/(\d+)/$', core_views.ConflictInterestDetailsView.as_view(), name='conflict-interest-details'),

    url(r'^datasets/family-member-companies/$', core_views.FamilyMemberCompaniesView.as_view(), name='family-member-companies'),
    url(r'^datasets/family-member-companies/(\d+)/$', core_views.FamilyMemberCompanyDetailsView.as_view(), name='family-member-company-details'),

    url(r'^datasets/conflict-interest-family-members/$', core_views.ConflictInterestFamilyMembersView.as_view(), name='conflict-interest-family-members'),
    url(r'^datasets/conflict-interest-family-members/(\d+)/$', core_views.ConflictInterestFamilyMemberDetailsView.as_view(), name='conflict-interest-family-member-details'),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += patterns(
    'django.views.static', (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}), )

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += patterns('',
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     )
