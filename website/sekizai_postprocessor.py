# -*- coding: utf-8 -*-
"""
 Get django-sekizai, django-compessor (and django-cms) playing nicely together
 re: https://github.com/ojii/django-sekizai/issues/4
 using: https://github.com/jezdez/django_compressor.git
 and: https://github.com/ojii/django-sekizai.git@0.5
"""
from compressor.templatetags.compress import CompressorNode
from django.template.base import *

def compress(context, data, name):
    """
    Data is the string from the template (the list of js files in this case)
    Name is either 'js' or 'css' (the sekizai namespace)

    We basically just manually pass the string through the {% compress 'js' %} template tag
    """
    return CompressorNode(Template(data).nodelist, name, 'file').render({})
