#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# activities app URL mappings.
#
# Created on 2008-10-28.
# $Id: urls.py 26 2009-08-04 22:06:00Z guolin.mobi $
#

from django.conf.urls.defaults import patterns

urlpatterns = patterns( "afcpweb.apps.activities.views",
    
    ( r"^home/$"                           , "home"              ),
    #( r"^(?P<uid>\w+)/$"           	   , "show_activity"     ),
    ( r"^2012gala/$"                       , "gala_announce"     ),
	( r"^2011ete/$"				           , "summer_travel"     ),
    ( r"^afcp_election/$"                  , "afcp_election"     ),
    ( r"^feichengwurao/$"                  , "feichengwurao"     ),
	( r"^2011ete/inscription/$"   		   , "travel_inscript"   ),
	( r"^2011navigate/$"				   , "summer_navigate"	 ),
	( r"^2011navigate/inscription/$"	   , "navigate_inscript" ),
	( r"^2011gala/inscription/$"		   , "gala_inscript"	 ),
	( r"^2011thermal/inscription/$" 	   , "thermal_inscript"	 ),
    ( r"^2013ski/inscription/$" 	   	   , "ski_inscript"  ),
    ( r"^2012paybas/inscription/$" 	   	   , "spring_travel_2012_inscript"  ),
)


#
