#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created on 2008-05-06.
# $Id: views.py 26 2009-08-04 22:06:00Z guolin.mobi $
#

import logging

from django.template import loader
from django.template import Context
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from google.appengine.api import users

from afcpweb.apps.common.actions import get_common_data

#---------------------------------------------------------------------------------------------------
# Sub-webapp homepages
#---------------------------------------------------------------------------------------------------


def _redirect_to_error_page(error):
    params = { "error" : error, }
    url = "/error/?%s" % ( urllib.urlencode(params))
    return HttpResponseRedirect(url)

def _afcp_home(request):
    return HttpResponseRedirect("/afcp/")

def _default_home(request):
    return _afcp_home(request)


HOME_HANDLER_MAPPINGS = {  "afcp" : _afcp_home, }

SERVER_HANDLER_MAPPINGS = { "www.afcp-paristech.org"    : _afcp_home,
                            "beta.afcp-paristech.org"   : _afcp_home,
                            "afcp.appspot.com"          : _afcp_home, }

#---------------------------------------------------------------------------------------------------
# Homepage handler
#---------------------------------------------------------------------------------------------------

def home(request):
    home = request.REQUEST.get("home")
    handler = HOME_HANDLER_MAPPINGS.get(home, None)
    if handler is not None:
        return handler(request)
    else:
        server = request.META.get("SERVER_NAME")
        handler = SERVER_HANDLER_MAPPINGS.get(server, None)
        if handler is not None:
            return handler(request)
        else:
            return _default_home(request)


def not_found(request):
    "Renders the 404 not-found page."
    
    logging.info("The requested page '%s' does not exist." % request.path)
    ctxt_dict = { "url": request.path, }
    ctxt_dict.update(get_common_data(request))
    ctxt = Context(ctxt_dict)
    tmpl = loader.get_template("not_found.html")
    return HttpResponse(tmpl.render(ctxt))


def error_page(request):
    "Displays the error page."
    
    ctxt_dict = { "error" : utils.get_param(request.REQUEST, "error"), }
    ctxt_dict.update(get_common_data(request))
    ctxt = Context(ctxt_dict)
    tmpl = loader.get_template("error.html")
    return HttpResponse(tmpl.render(ctxt))



#