# -*- coding: utf-8 -*-
"""Fab commands that are running locally."""

import os

from fabric import colors
from fabric.api import *
from fabric.contrib import django

django.settings_module('website.settings')
try:
    from django.conf import settings
except ImportError:
    pass


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
    local('python manage.py makemessages -a -i "env*"')
    local('python manage.py makemessages -d djangojs -a -i "env*"')


def mo():
    """Compile all message catalogs."""
    local('python manage.py compilemessages')


def init_git():
    """Initialize the git repository."""
    rmdir('.git')
    local('git init')
    remove('.gitignore')
    rename('gitignore', '.gitignore')
    local('git add -A')
    local('git commit -m "Initial commit."')
    local('git branch -m develop')
    local('git checkout -b master')


def devserver(host='localhost', port=8000):
    """Start development server."""
    local('python manage.py runserver %s:%s' % (host, port))


def syncdb():
    """Sync database."""
    local('python manage.py syncdb --all')
    local('python manage.py migrate --fake')
