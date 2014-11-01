#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Feed info
# 
# Created on 2008-11-19.
# $Id: planet.py 41 2010-07-21 10:33:30Z guolin.mobi $
#

class PlanetFeed(object):
    def __init__(self, site_name, site_link, feed_link, author):
        self.site_name = site_name
        self.site_link = site_link
        self.feed_link = feed_link
        self.author    = author


FEEDS = ( 
	  PlanetFeed( site_name="挣扎中成长",
                      site_link="http://heavyz.blogspot.com/",
                      feed_link="http://heavyz.blogspot.com/feeds/posts/default",
                      author="郑重" ),

          PlanetFeed( site_name="不过尔尔",
                      site_link="http://lincode.blogbus.com/",
                      feed_link="http://lincode.blogbus.com/index.rdf",
                      author="郭麟" ),


          # Add your site feed here:
          # PlanetFeed( site_name="Your Site Name",
          #             site_link="Your Site URL",
          #             feed_link="Your Site Feed URL",
          #             author="Your Name" ),

        ) # FEEDS

PHOTOS = (

            PlanetFeed( site_name="郑重的 Flickr 相册",
                      site_link="http://www.flickr.com/photos/zhengzhong/",
                      feed_link="http://api.flickr.com/services/feeds/photos_public.gne?id=24660842@N03",
                      author="郑重" ),

            PlanetFeed( site_name="afcp picasa 相集",
                      site_link="http://picasaweb.google.fr/AFCParisTech",
                      feed_link="http://picasaweb.google.fr/data/feed/base/user/AFCParisTech/albumid/5340989829803111505",
                      author="afcp" ),			  
					  

		)

