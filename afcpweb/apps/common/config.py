#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# AFCP webapp global configurations.
#
# Created on 2008-10-28.
# $Id: config.py 26 2009-08-04 22:06:00Z guolin.mobi $
#

class Config(object):
    """This class contains constants for the AFCP webapp."""

    APP_NAME      = "common"
    
    STATIC_PREFIX = "/static"
    VERSION       = "0.1"
    REVISION      = "$Revision: 300 $"
    REVISED_DATE  = "$Date: 2009-08-05 00:06:00 +0200 (10, 05  8 2009) $"
    ADMINS        = ( "AFCParisTech[suffix]".replace("[suffix]", "@gmail.com"),
					   "guolin.mobi[suffix]".replace("[suffix]", "@gmail.com"),
					   "afcpweb[suffix]".replace("[suffix]", "@gmail.com") )
