from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # Authentication
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # API
    url(r'^', include(router.urls)),
)
