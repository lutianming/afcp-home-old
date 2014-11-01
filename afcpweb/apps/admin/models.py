#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Datastore model classes for admin app. 
#
# Created on 2010-07-18.
# $Id: models.py 29 2010-07-18 21:22:49Z guolin.mobi $
#

from google.appengine.ext import db

class AFCPActivity(db.Model):
    "This class represents an Activity"
    
    uid         = db.StringProperty(required=True)
    name        = db.StringProperty(required=True)
    subject     = db.StringProperty()
    date        = db.DateTimeProperty()
    address     = db.StringProperty()
    spreadsheet_link = db.StringProperty()
    create_date = db.DateTimeProperty(auto_now_add=True)
    is_closed   = db.StringProperty(choices=["yes", "no"], default="no")

    @classmethod
    def find_all(cls, **kwargs):
        query = cls.all()
        return query
    
    @classmethod
    def get_unique(cls, uid):
        instance = cls.gql("WHERE uid=:uid", uid=uid).get()
        return instance

#