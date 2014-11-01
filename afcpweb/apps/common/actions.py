#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# afcpweb app commom actions.
#
# Created on 2008-10-28.
# $Id: urls.py 26 2009-08-04 22:06:00Z guolin.mobi $
#

import urllib

from afcpweb.apps.common.config import Config
from afcpweb.apps.members.models import get_current_user
from afcpweb.apps.members.models import create_login_url
from afcpweb.apps.members.models import create_logout_url


#---------------------------------------------------------------------------------------------------
# Language class
#---------------------------------------------------------------------------------------------------

class Language(object):
    
    LANG_SESSION_NAME = "django_language"
    
    ENGLISH_CODE = "en"
    FRENCH_CODE  = "fr"
    CHINESE_CODE = "zh-cn"
    
    DEFAULT_LANG_CODE    = FRENCH_CODE
    SUPPORTED_LANG_CODES = (  FRENCH_CODE, CHINESE_CODE, )
   
    def __init__(self, code, url, is_current):
        self.code = code
        self.url = url
        self.is_current = is_current
    
    @staticmethod
    def create_lang_url(redirect_url, lang_code):
        params = { "url" : redirect_url, "lang" : lang_code, }
        url = "/%s/lang/?%s" % ( Config.APP_NAME, urllib.urlencode(params))
        return url
    
    @staticmethod
    def get_lang(request):
        try:
            lang_code = request.session.get(Language.LANG_SESSION_NAME, None)
        except AttributeError:
            lang_code = Language.DEFAULT_LANG_CODE
        return lang_code
    
    @staticmethod
    def set_lang(request, lang_code):
        try:
            request.session[Language.LANG_SESSION_NAME] = lang_code
            return True
        except AttributeError:
            return False


#---------------------------------------------------------------------------------------------------
# Common functions
#---------------------------------------------------------------------------------------------------
   

def get_common_data(request):

    # User info.
    user = get_current_user()
    if not user:
        log_url  = create_login_url("%s/login_ok/%s" % ( Config.APP_NAME, request.path,))
        log_text = "Login"
        is_admin = False
    else:
        log_url  = create_logout_url("%s/login_ok/%s" % ( Config.APP_NAME, request.path,))
        log_text = "Logout"
        is_admin = (user.email() in Config.ADMINS)

    # Language.
    current_lang_code = Language.get_lang(request)
    languages = []
    for lang_code in Language.SUPPORTED_LANG_CODES:
        lang_url    = Language.create_lang_url(request.path, lang_code)
        is_current  = (lang_code == current_lang_code)
        languages.append(Language(lang_code, lang_url, is_current))    
    
    # Request meta info.
    http_referer = request.META.get("HTTP_REFERER", "unknown_http_referer")
    remote_addr  = request.META.get("REMOTE_ADDR" , "unknown_remote_addr" )
    remote_host  = request.META.get("REMOTE_HOST" , "unknown_remote_host" )   

    # Return the common context dict.
    return { "user_"            : user,
             "log_url_"         : log_url,
             "log_text_"        : log_text,
             "is_admin_"        : is_admin,
             "languages_"       : languages,
             "http_referer_"    : http_referer,
             "remote_addr_"     : remote_addr,
             "remote_host_"     : remote_host,
             "static_"          : Config.STATIC_PREFIX }


#