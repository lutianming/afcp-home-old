#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Admin app URL mappings.
#
# Created on 2008-10-28.
# $Id: urls.py 40 2010-03-08 23:05:09Z guolin.mobi $
#

from django.conf.urls.defaults import patterns

urlpatterns = patterns( "afcpweb.apps.admin.views",

    ( r"^$"	     		                   , "admin" 		       ),
    ( r"^activity/$"	     	           , "view_all_activity"   ),
    ( r"^activity/create/$"                , "create_activity" 	   ),
    ( r"^activity/create/(?P<uid>\w+)/$"   , "create_activity" 	   ),
    ( r"^activity/delete/(?P<uid>\w+)/$"   , "delete_activity" 	   ),
    ( r"^activity/(?P<uid>\w+)/$"	   	   , "view_activity" 	   ),
)

#

