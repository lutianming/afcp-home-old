#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Views for the global app.
#
# Created on 2008-10-28.
# $Id: views.py 40 2010-03-08 23:05:09Z guolin.mobi $
#

from django.http import HttpResponseRedirect

from afcpweb.apps.members.models import get_current_user
from afcpweb.apps.common import utils
from afcpweb.apps.common.actions import Language


def login_ok(request, url):
    try:
        profile = get_current_user().profile()
        if profile:
            profile.count_login()
            profile.put()
    except:
        pass
    return HttpResponseRedirect(url)


def logout_ok(request, url):
    return HttpResponseRedirect(url)


#---------------------------------------------------------------------------------------------------
# Change current language and logged-in/logged-out redirect
#---------------------------------------------------------------------------------------------------


def change_language(request):
    "Change the current language."
    
    redirect_url = utils.get_param(request.REQUEST, "url" )
    lang_code    = utils.get_param(request.REQUEST, "lang")
    Language.set_lang(request, lang_code)
    return HttpResponseRedirect(redirect_url)


#