# -*- coding: utf-8 -*-
"""Basic configuration for this Django project."""

import os

from {{ project_name }}.settings import *

PROJECT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__),
                               '..', '..'))

gettext = lambda s: s

DEBUG = False

TEMPLATE_DEBUG = DEBUG

ADMINS = (
)

MANAGERS = ADMINS

LANGUAGES = [
    ('de', gettext(u'German')),
]

TIME_ZONE = 'Europe/Berlin'

LANGUAGE_CODE = 'de-de'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'staticfiles', 'media')

STATIC_ROOT = os.path.join(PROJECT_DIR, 'staticfiles', 'static')

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.urls'

INSTALLED_APPS = (
    '{{ project_name }}.website',
    # Custom administration
    'admin_shortcuts',
    'djangocms_admin_style',
    # Default Django apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    # For Django-CMS
    'cms',
    'mptt',
    'menus',
    'sekizai',
    'cms.plugins.text',
    'cms.plugins.link',
    'cms.plugins.picture',
    # Widgets
    'tinymce',
    # Other
    'easy_thumbnails',
    'south',
    'compressor',
    'django_rj_utils',
    'bootstrap_toolkit',
    'bootstrap-pagination',
    'piwik',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, '{{ project_name }}', 'website', 'templates',
                 'website'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'sekizai.context_processors.sekizai',
)

WSGI_APPLICATION = 'website.wsgi.application'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

LOCALE_PATHS = [
    os.path.join(PROJECT_DIR, '{{ project_name }}', 'locale'),
]

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

# DjangoCMS
# Cannot be empty!
CMS_TEMPLATES = (
    ('default.html', 'Default'),
)

CMS_MENU_TITLE_OVERWRITE = True

CMS_USE_TINYMCE = True

#CMS_PLACEHOLDER_CONF = {
#}

# TinyMCE
TINYMCE_DEFAULT_CONFIG = {
    'plugins': 'spellchecker, contextmenu, advlist, style, paste, lists, '
        'fullscreen',
    'theme': 'advanced',
    'skin': 'o2k7',
    'entity_encoding': 'raw',
    'theme_advanced_resizing': '',
    'theme_advanced_toolbar_location': 'top',
    'theme_advanced_toolbar_align': 'left',
    'theme_advanced_buttons1': 'bold, italic, underline, |, justifyleft, '
        'justifycenter, justifyright, justifyfull, |, bullist, numlist, '
        'outdent, indent, |, code, |, fullscreen',
    'theme_advanced_buttons2': '',
    'width': '800',
    'height': '350',
}

TINYMCE_SPELLCHECKER = True

# Important! Less must be installed: http://lesscss.org/#-server-side-usage
COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)

# Admin Shortcuts
ADMIN_SHORTCUTS = [
    {
        'shortcuts': [
            {
                'url': '/',
            },
            {
                'url_name': 'admin:cms_page_changelist',
                'title': _(u'Pages'),
            },
        ]
    },
]
