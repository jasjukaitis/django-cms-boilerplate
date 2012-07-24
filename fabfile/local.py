# -*- coding: utf-8 -*-
"""Fab commands that are running locally."""

import os

from fabric import colors
from fabric.api import *
from fabric.contrib import django

django.settings_module('{{ project_name }}.settings')
try:
    from django.conf import settings
except ImportError:
    pass


MANAGEPY = '%s/manage.py' % settings.PROJECT_DIR


def init_project():
    """Initialize the project."""
    install_dev_requirements()
    syncdb()
    mo()
    # Clean README
    open('README.rst', 'w').close()
    init_git()


def install_stable_requirements():
    """Install requirements for production."""
    local('pip install -Ur requirements/stable.req.txt')


def install_dev_requirements():
    """Install requirements for development."""
    local('pip install -Ur requirements/development.req.txt')
    install_stable_requirements()


def po():
    """Generate message catalog for all languages."""
    with lcd(os.path.join(settings.PROJECT_DIR, 'website')):
        local('python %s makemessages -a -i "env*"' % MANAGEPY)
        local('python %s makemessages -d djangojs -a -i "env*"' % MANAGEPY)


def mo():
    """Compile all message catalogs."""
    with lcd(os.path.join(settings.PROJECT_DIR, '{{ project_name }}')):
        local('python %s compilemessages' % MANAGEPY)


def init_git():
    """Initialize the git repository."""
    local('git init')
    os.rename('gitignore', '.gitignore')
    local('git add -A')
    local('git commit -m "Initial commit."')
    local('git branch -m develop')
    local('git checkout -b master')


def devserver(host='localhost', port=8000):
    """Start development server."""
    local('python %s runserver %s:%s' % (MANAGEPY, host, port))


def syncdb():
    """Sync database."""
    local('python %s syncdb --all' % MANAGEPY)
    local('python %s migrate --fake' % MANAGEPY)
