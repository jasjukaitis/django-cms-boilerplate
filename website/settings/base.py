# -*- coding: utf-8 -*-
"""Basic configuration for this Django project."""

import os

from website.settings import *

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

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'website', 'media')

STATIC_ROOT = os.path.join(PROJECT_DIR, 'website', 'static')

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'website.urls'

INSTALLED_APPS = (
    'website',
    # Custom administration
    #'admintools_bootstrap',
    'admin_tools.dashboard',
    #'admin_tools.menu',
    #'admin_tools.theming',
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
    # Further admin stuff
    'dashboardmods',
    'filer',
    # CMS extensions
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',
    # Widgets
    'tinymce',
    # Other
    'easy_thumbnails',
    # Deployment stuff
    'gunicorn',
    'south',
    'raven.contrib.django',
    'compressor',
    # XStatic
    'xstatic',
    'xstatic.pkg.jquery',
    'xstatic.pkg.bootstrap',
    'xstatic.pkg.less',
    'xstatic.pkg.html5shiv',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django_xstatic.finders.XStaticFinder',
    'compressor.finders.CompressorFinder',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'website', 'templates', 'website'),
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
    'django_xstatic.finders.XStaticFinder',
    'compressor.finders.CompressorFinder',
)

LOCALE_PATHS = [
    os.path.join(PROJECT_DIR, 'website', 'locale'),
]

# Administration
ADMIN_TOOLS_INDEX_DASHBOARD = 'website.dashboard.IndexDashboard'

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
