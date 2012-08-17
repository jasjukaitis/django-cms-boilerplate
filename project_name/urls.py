# -*- coding: utf-8 -*-
"""URLs for the website."""

from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import direct_to_template

from cms.sitemaps import CMSSitemap

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {
        'sitemaps': {
            'cmspages': CMSSitemap,
        }
    }),
    url(r'^robots\.txt$', direct_to_template,
        {'template': 'robots.txt', 'mimetype': 'text/plain'}),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^', include('filer.server.urls')),
    url(r'^', include('cms.urls')),
)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += (
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,}),
    )
