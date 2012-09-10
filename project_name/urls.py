from django.conf import settings
from django.conf.urls import patterns, include, url, handler404, handler500
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import direct_to_template


handler404 = '{{ project_name }}.views.page_not_found'
handler500 = '{{ project_name }}.views.server_error'
admin.autodiscover()


urlpatterns = patterns('',
  url(
    r'^$',
    direct_to_template,
    {'template': 'home.jade'},
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
  urlpatterns += patterns('', url(r'^404/$', direct_to_template, {'template': '404.jade'}))
  urlpatterns += patterns('', url(r'^500/$', direct_to_template, {'template': '500.jade'}))
  