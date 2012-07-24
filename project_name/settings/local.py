# -*- coding: utf-8 -*-
"""All local configuration (e.g. SECRET_KEY or DATABASES)."""

from {{ project_name }}.settings import *

SECRET_KEY = '{{ secret_key }}'
