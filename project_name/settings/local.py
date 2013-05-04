# -*- coding: utf-8 -*-
"""All local configuration (e.g. SECRET_KEY or DATABASES)."""

from {{ project_name }}.settings import *

SECRET_KEY = '{{ secret_key }}'


#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': '',
#        'USER': '',
#        'PASSWORD': '',
#        'HOST': '',
#        'PORT': '',
#    },
#}

#SENTRY_DSN = ''

# Piwik
#PIWIK_SITE_ID = 0
#PIWIK_URL = ''
