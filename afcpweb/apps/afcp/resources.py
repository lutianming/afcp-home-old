#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2008 ZHENG Zhong <heavyzheng nospam-at gmail D0T com>
# - http://heavyz.blogspot.com/
# - http://buggarden.blogspot.com/
#
# Created on 2008-12-08.
# $Id: resources.py 26 2009-08-04 22:06:00Z guolin.mobi $
#

class BannerImage(object):
    def __init__(self, id, url, title, desc):
        self.id    = id
        self.url   = url
        self.title = title
        self.desc  = desc


BANNER_IMAGES = ( BannerImage( id="header_forum",
                               url="/forum/home/fr/",
                               title="",
                               desc="" ),
#                 BannerImage( id="header_1",
#                               url="http://afcp-paristech.blogspot.com/2011/09/2011-afcpgala-de-la-lune.html",
#                               title="",
#                               desc="" ),
                  
#                  BannerImage( id="header_2",
#                               url="/afcp/",
#                               title="Conférence AFCP ",
#                               desc="Taken by AFCP on 2009-3-22" ),
#				  
#				  BannerImage( id="header_3",
#                               url="/forum/",
#                               title="Forum Horizon Chine",
#                               desc="Taken by AFCP on 2008-5-22" ),
#                  
#				  BannerImage( id="header_4",
#                               url="/afcp/",
#                               title="Conférence AFCP",
#                               desc="Taken by AFCP on 2008-5-22" ),
#				
#				  BannerImage( id="header_5",
#                               url="/afcp/",
#                               title="Conférence AFCP",
#                               desc="Taken by AFCP on 2009-3-22" ),
#					
#				  BannerImage( id="header_6",
#                               url="/forum/",
#                               title="Forum Horizon Chine",
#                               desc="Taken by AFCP on 2008-5-22" ),	
                  # Add a banner image here:
                  # BannerImage( id="id (static image file base name)",
                  #              url="external url",
                  #              title="image title",
                  #              desc="description" ),
                ) # BANNER_IMAGES


contactus_emails = u'AFCP <AFCParisTech@gmail.com>, guan.pengpourss@gmail.com, realzhq@gmail.com'
