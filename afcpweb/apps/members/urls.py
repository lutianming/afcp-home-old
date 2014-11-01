#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Inscription app URL mappings.
#
# Created on 2008-10-28.
# $Id: urls.py 26 2009-08-04 22:06:00Z guolin.mobi $
#

from django.conf.urls.defaults import patterns

urlpatterns = patterns( "afcpweb.apps.members.views",
    
    ( r"^$"                                   , "view_members"       ),
    ( r"^my_profile/$"                        , "my_profile"         ),
    ( r"^profile/(?P<uid>\w+)/$"              , "profile"            ),
    ( r"^profile/(?P<uid>\w+)/photo/$"        , "profile_photo"      ),
    ( r"^random_profile/$"                    , "random_profile"     ),
    ( r"^ecole/(?P<acronym>\w+)/$"            , "ecole"              ),
    ( r"^university/(?P<acronym>\w+)/$"       , "university"         ),
)


#