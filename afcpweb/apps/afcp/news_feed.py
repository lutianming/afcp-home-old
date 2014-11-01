#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2008 ZHENG Zhong <heavyzheng nospam-at gmail D0T com>
# - http://heavyz.blogspot.com/
# - http://buggarden.blogspot.com/
#
# Created on 2008-11-19.
# $Id: newsFeed.py 26 2009-08-04 22:06:00Z guolin.mobi $
#

class NewsFeed(object):
    def __init__(self, site_name, site_link, feed_link, author):
        self.site_name = site_name
        self.site_link = site_link
        self.feed_link = feed_link
        self.author    = author


FEEDS = ( 
			NewsFeed( site_name="AFCP Blog",
                      site_link="http://afcp-paristech.blogspot.com/",
                      feed_link="http://afcp-paristech.blogspot.com/feeds/posts/default",
                      author="AFCP Blogger" ),
			NewsFeed( site_name="AFCP Petites Annonces",
                      site_link="http://afcppetitesannonces.blogspot.com/",
                      feed_link="http://afcppetitesannonces.blogspot.com/feeds/posts/default",
                      author="AFCP Petites Annonces" ),
           # NewsFeed( site_name="AFCP Loisir",
           #           site_link="http://mmhancxt.blogspot.com/",
           #           feed_link="http://mmhancxt.blogspot.com/feeds/posts/default",
           #           author="LIU Liang" ),
                      
          # Add your site feed here:
          # NewsFeed( site_name="Your Site Name",
          #             site_link="Your Site URL",
          #             feed_link="Your Site Feed URL",
          #             author="Your Name" ),

        ) # FEEDS
