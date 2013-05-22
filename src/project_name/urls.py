from django.conf import settings
from django.conf.urls import patterns, include, url, handler404, handler500
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView


repr(handler404)
repr(handler500)
handler404 = '{{ project_name }}.views.page_not_found'
handler500 = '{{ project_name }}.views.server_error'


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(
        r'^$',
        TemplateView.as_view(template_name='home.html'),
        name='home'
    ),

    # Admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

# Serve media files locally in DEBUG mode
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Debug error pages
if settings.DEBUG:
    urlpatterns += patterns(
        '', url(r'^404/$', TemplateView.as_view(template_name='404.html')))
    urlpatterns += patterns(
        '', url(r'^500/$', TemplateView.as_view(template_name='500.html')))