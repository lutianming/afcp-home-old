#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Access for admin app. 
#
# Created on 2010-07-18.
# $Id: models.py 29 2010-07-18 21:22:49Z guolin.mobi $
#

from afcpweb.apps.common.access import Access

class AdminAccess(Access):
        
    def can_consult(self):
        return is_webmaster(self._user)

    def can_edit(self):
        return is_webmaster(self._user)

#