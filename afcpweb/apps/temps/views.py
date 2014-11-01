#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Views for the temps app.
#
# Created on 2008-07-18.
# $Id: views.py 40 2010-03-08 23:05:09Z guolin.mobi $
#

import logging

from django.template import loader
from django.template import Context
from django.http import HttpResponse

from afcpweb.apps.common.actions import get_common_data

from afcpweb.apps.temps.config import Config 


def view_spring(request):
    """Displays the spring."""
   
    ctxt_dict = {}
                  
    ctxt_dict.update(get_common_data(request))
    ctxt = Context(ctxt_dict)
    tmpl = loader.get_template("%s/spring.html" % Config.APP_NAME)
    return HttpResponse(tmpl.render(ctxt))


#