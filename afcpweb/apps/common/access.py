#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Access for global app. 
#
# Created on 2010-07-18.
# $Id: models.py 29 2010-07-18 21:22:49Z guolin.mobi $
#

from afcpweb.apps.common.config import Config

def is_webmaster(user):
    if not user:
        return False
    else:
        return user.email() in Config.ADMINS
    
class Access(object):
    
    def __init__(self, user):
        self._user = user
        
    def is_webmaster(self):
        return is_webmaster(sef._user)