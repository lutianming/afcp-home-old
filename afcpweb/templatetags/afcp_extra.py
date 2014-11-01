#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created on 2009-11-18.
# $Id$
#

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def mark_escape(value):
    return mark_safe(value)
    

# EOF
