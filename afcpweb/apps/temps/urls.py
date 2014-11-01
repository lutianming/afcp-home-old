#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# temps app URL mappings.
#
# Created on 2008-10-28.
# $Id: urls.py 26 2009-08-04 22:06:00Z guolin.mobi $
#

from django.conf.urls.defaults import patterns

urlpatterns = patterns( "afcpweb.apps.temps.views",
    
    ( r"^$"                             , "view_spring" ),
    ( r"^spring/$"	                    , "view_spring" ),
)


#