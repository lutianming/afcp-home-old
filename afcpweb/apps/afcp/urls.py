#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# AFCP webapp URL mappings.
#
# Created on 2008-10-28.
# $Id: urls.py 41 2010-07-21 10:33:30Z guolin.mobi $
#

from django.conf.urls.defaults import patterns

urlpatterns = patterns( "afcpweb.apps.afcp.views",

    ( r"^$"                                         , "home"         ),
	
    ( r"^static/about/$"		            , "about"        ),	
    ( r"^static/about/(?P<name>\w+)/$"              , "about"        ),
    ( r"^static/about/(?P<name>\w+)/(?P<lang>.+)/$" , "about"        ),
    ( r"^static/contact/$"			    , "contact"	     ),	
    ( r"^static/contact/(?P<lang>\w+)/$"            , "contact"      ),	
    
    ( r"^news/$"                     	            , "news"         ),
    ( r"^afcpchine/$"                               , "afcpchine"    ),
    ( r"^afcpchine/alumnisalon/$"                   , "alumnisalon"  ),
    ( r"^amusement/$"                               , "amusement"    ),
    ( r"^amusement/planet/$"                 	    , "planet_afcp"  ),
    ( r"^amusement/photos/$"                 	    , "photos_afcp"  ),
    ( r"^amusement/bal/$"                           , "bal"  ),
    ( r"^amusement/gala/$"                          , "gala"  ),
    ( r"^amusement/lanternes/$"                     , "lanternes"  ),
    ( r"^research/$"                                , "research"  ),
    ( r"^research/presentation/$"                   , "presentation"  ),
    ( r"^research/training/$"                       , "training"  ),
    ( r"^research/workpermit/$"                     , "workpermit"  ),
    ( r"^misc/$"                                    , "misc"  ),
    ( r"^misc/itineraire-x/$"                       , "itineraireX"  ),
    ( r"^misc/seminaire/$"                          , "seminaire"  ),
    ( r"^misc/training/$"                           , "training_old"  ),
    ( r"^misc/roundtable/$"                         , "roundtable"  ),
    ( r"^misc/nuitdechine/$"                        , "nuitdechine"  ),
    
)

