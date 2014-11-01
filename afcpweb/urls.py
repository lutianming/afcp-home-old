#!/usr/bin/python
# -*- coding: utf-8 -*-
#

# $Id: urls.py 26 2009-08-04 22:06:00Z guolin.mobi $
#

# Django URL mappings.

from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import include

urlpatterns = patterns( "",
    # Sub-webapps in the bug garden.
    ( r"^afcp/"         , include("afcpweb.apps.afcp.urls") ),
    ( r"^activities/"   , include("afcpweb.apps.activities.urls") ),
    ( r"^admin/"        , include("afcpweb.apps.admin.urls") ),
    ( r"^common/"       , include("afcpweb.apps.common.urls") ),    
    ( r"^forum/"        , include("afcpweb.apps.forum.urls") ),
    ( r"^members/"      , include("afcpweb.apps.members.urls") ),
    ( r"^temps/"        , include("afcpweb.apps.temps.urls") ),
    # Top-level URL mappings.
    ( r"^$", "afcpweb.apps.misc.views.home" ),
    # 404 not-found to catch all (this should always be the last URL pattern).
    ( r"^.*$/", "afcpweb.apps.misc.views.not_found"),
)


