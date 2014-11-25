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
    url(r'^datasets/', core_views.DatasetsView.as_view(), name='datasets'),


    url(r'^faq/', core_views.FaqView.as_view(), name='faq'),
    url(r'^about/', core_views.AboutView.as_view(), name='about'),
    url(r'^contact/', core_views.ContactView.as_view(), name='contact'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

    urlpatterns += patterns(
        'django.views.static', (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}), )