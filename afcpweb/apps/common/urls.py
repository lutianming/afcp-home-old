#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Common URL mappings.
#
# Created on 2008-10-28.
# $Id: urls.py 26 2009-08-04 22:06:00Z guolin.mobi $
#

from django.conf.urls.defaults import patterns

urlpatterns = patterns( "afcpweb.apps.common.views",
    
    ( r"^login_ok/(?P<url>.*)$"               , "login_ok"           ),
    ( r"^logout_ok/(?P<url>.*)$"              , "logout_ok"          ),
    ( r"^lang/$"                              , "change_language"    ),
	# 404 not-found: must be the last URL pattern.
    ( r"^.*$"                                  , "not_found"   ),
)