from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from apps.core import views as core_views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('userena.urls')),
    url(r'^serbia/', include('apps.serbia.urls', namespace='serbia')),
    url(r'^usa/', include('apps.usa.urls', namespace='usa')),
    url(r'^montenegro/', include('apps.core.urls', namespace='montenegro')),
    url(r'^', include('apps.corex.urls')),


    url(r'^search', core_views.SearchView.as_view(), name='search'),




) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += patterns('django.views.static',
                        (r'media/(?P<path>.*)', 'serve',
                         {'document_root': settings.MEDIA_ROOT}), )

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += patterns('',
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     )
