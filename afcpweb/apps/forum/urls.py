#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#
# Forum app URL mappings.
#
# Created on 2008-10-28.
# $Id: urls.py 41 2010-07-21 10:33:30Z guolin.mobi $
#

from django.conf.urls.defaults import patterns

urlpatterns = patterns( "afcpweb.apps.forum.views",

#    ( r"^lang/$"                              		, "change_language"    ),
#    
#	( r"^$"                                   		, "home"     ), 
#	( r"^home/$"                     	  	  		, "home"     ),
#	( r"^home/(?P<lang>.+)/$"                 		, "home"     ),	
#
#	( r"^inscription/$"								, "inscription" ),
#	( r"^inscription$"								, "inscription" ),
#
#	( r"^visitors/$"      							, "visitor"     ),
#	#( r"^visitors/(?P<name>\w+)$"      				, "visitor"     ),
#	( r"^visitors/(?P<name>\w+)/(?P<lang>.+)/$"     , "visitor"     ),
#	( r"^visitors/(?P<name>\w+)"     				, "visitor"     ),
#
#	
#	( r"^exhibitors/$"      						, "exhibitor"     ),
#	( r"^exhibitors/(?P<name>\w+)$"      			, "exhibitor"     ),
#	( r"^exhibitors/(?P<name>\w+)/(?P<lang>.+)/$"   , "exhibitor"     ),
#	
#	( r"^contact/$"                    				, "contact"     ),
#	( r"^contact/(?P<name>\w+)$"                    , "contact"     ),
#    ( r"^contact/(?P<name>\w+)/(?P<lang>.+)/$"      , "contact"     ),
#
#	#( r"^inscript/$"								, "saint_gobain"),
#	( r"^inscript/(?P<name>\w+)$"					, "inscript"),
#	( r"^inscript/(?P<name>\w+)/(?P<lang>.+)/$"		, "inscript"),
#
#	# 404 not-found: must be the last URL pattern.
#    ( r"^.*$"                                 		, "not_found"   ),

    # Redirection vers le nouveau site du Forum Horizon Chine
    ( r"^.*$"                                         , "redirect_to_new_website"   ),
)

