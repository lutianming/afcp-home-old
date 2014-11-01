#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Views for the members app.
#
# Created on 2008-10-28.
# $Id: views.py 40 2010-03-08 23:05:09Z guolin.mobi $
#

import logging

from django.template import loader
from django.template import Context
from django.http import HttpResponse
from afcpweb.apps.activities.config import Config
from afcpweb.apps.common.actions import get_common_data
from afcpweb.apps.activities.models import AFCPActivity

def home(request):
    ctxt_dict = {}
    ctxt_dict.update(get_common_data(request))
    ctxt = Context(ctxt_dict)
    tmpl = loader.get_template("%s/home.html" % Config.APP_NAME)
    return HttpResponse(tmpl.render(ctxt))

def show_activity(request,uid):

    activity = AFCPActivity.get_unique(uid)
    if request.method == "GET":
        ctxt_dict = { "activity"      : activity,}
        ctxt_dict.update(get_common_data(request))
        ctxt = Context(ctxt_dict)
        tmpl = loader.get_template("%s/show_activity.html" % Config.APP_NAME)
        return HttpResponse(tmpl.render(ctxt))
    else :
        return not_found(request)

def summer_travel(request):
    ctxt_dict = {}
    ctxt_dict.update(get_common_data(request))
    ctxt = Context(ctxt_dict)
    tmpl = loader.get_template("%s/summer_travel.html" % Config.APP_NAME)
    return HttpResponse(tmpl.render(ctxt))

def travel_inscript(request):
    ctxt_dict = {}
    ctxt_dict.update(get_common_data(request))
    ctxt = Context(ctxt_dict)
    tmpl = loader.get_template("%s/travel_inscript.html" % Config.APP_NAME)
    return HttpResponse(tmpl.render(ctxt))

def summer_navigate(request):
    ctxt_dict = {}
    ctxt_dict.update(get_common_data(request))
    ctxt = Context(ctxt_dict)
    tmpl = loader.get_template("%s/summer_navigate.html" % Config.APP_NAME)
    return HttpResponse(tmpl.render(ctxt))

def navigate_inscript(request):
    ctxt_dict = {}
    ctxt_dict.update(get_common_data(request))
    ctxt = Context(ctxt_dict)
    tmpl = loader.get_template("%s/navigate_inscript.html" % Config.APP_NAME)
    return HttpResponse(tmpl.render(ctxt))
			
def gala_inscript(request):
    ctxt_dict = {}
    ctxt_dict.update(get_common_data(request))
    ctxt = Context(ctxt_dict)
    tmpl = loader.get_template("%s/gala_inscript.html" % Config.APP_NAME)
    return HttpResponse(tmpl.render(ctxt))

def thermal_inscript(request):
    ctxt_dict = {}
    ctxt_dict.update(get_common_data(request))
    ctxt = Context(ctxt_dict)
    tmpl = loader.get_template("%s/thermal_inscript.html" % Config.APP_NAME)
    return HttpResponse(tmpl.render(ctxt))
    
def ski_inscript(request):
    ctxt_dict = {}
    ctxt_dict.update(get_common_data(request))
    ctxt = Context(ctxt_dict)
    tmpl = loader.get_template("%s/ski2013wl.html" % Config.APP_NAME)
    return HttpResponse(tmpl.render(ctxt))
#

def spring_travel_2012_inscript(request):
    ctxt_dict = {}
    ctxt_dict.update(get_common_data(request))
    ctxt = Context(ctxt_dict)
    tmpl = loader.get_template("%s/spring_travel_2012.html" % Config.APP_NAME)
    return HttpResponse(tmpl.render(ctxt))
#

def feichengwurao(request):
    ctxt_dict = {}
    ctxt_dict.update(get_common_data(request))
    ctxt = Context(ctxt_dict)
    tmpl = loader.get_template("%s/feichengwurao.html" % Config.APP_NAME)
    return HttpResponse(tmpl.render(ctxt))

def gala_announce(request):
    ctxt_dict = {}
    ctxt_dict.update(get_common_data(request))
    ctxt = Context(ctxt_dict)
    tmpl = loader.get_template("%s/gala2012.html" % Config.APP_NAME)
    return HttpResponse(tmpl.render(ctxt))

def afcp_election(request):
    ctxt_dict = {}
    ctxt_dict.update(get_common_data(request))
    ctxt = Context(ctxt_dict)
    tmpl = loader.get_template("%s/afcp_election.html" % Config.APP_NAME)
    return HttpResponse(tmpl.render(ctxt))
