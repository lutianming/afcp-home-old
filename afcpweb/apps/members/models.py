#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Datastore model classes for the members.
#
# Created on 2008-10-28.
# $Id: models.py 29 2009-09-23 21:22:49Z guolin.mobi $
#

import logging
import datetime


from google.appengine.ext import db
from google.appengine.api import users

from afcpweb.apps.common import utils
from afcpweb.apps.members import paristech


class AFCPUserProfile(db.Model):
    """This class represents a profile of an AFCP member. The key name of the entity is the Google
    account email address.
    """
    
    MEMBER_ROLE = "member"
    EDITOR_ROLE = "editor"
    
    PENDING_STATUS  = "pending"
    APPROVED_STATUS = "approved"
    
    uid         = db.StringProperty(required=True)
    name        = db.StringProperty(required=True)
    name_zh     = db.StringProperty()
    sex         = db.StringProperty(choices=["male", "female", "unknown"], default="unknown")
    birthday    = db.DateTimeProperty()
    promo       = db.IntegerProperty()
    ecole_id    = db.StringProperty()
    univ_id     = db.StringProperty()
    alt_email   = db.StringProperty()
    tel         = db.StringProperty()
    
    photo_type  = db.StringProperty()
    photo_data  = db.BlobProperty()
    
    # cv_en         = props.CurriculumVitaeProperty(default=props.CurriculumVitae())
    # cv_fr         = props.CurriculumVitaeProperty(default=props.CurriculumVitae())
    # cv_zh         = props.CurriculumVitaeProperty(default=props.CurriculumVitae())
    
    status      = db.StringProperty(default=PENDING_STATUS)
    deleted     = db.BooleanProperty(default=False)
    create_date = db.DateTimeProperty(auto_now_add=True)
    last_login  = db.DateTimeProperty(auto_now_add=True)
    login_count = db.IntegerProperty(default=0)
    roles       = db.StringListProperty(default=[])
    
    def __unicode__(self):
        return self.user()

    def user(self):
        return users.User(self.key().name())
    
    def is_current_user_owner(self):
        user = users.get_current_user()
        return user == self.user()
    
    def google_account(self):
        return self.user().email()
    
    def names(self):
        names = self.name
        if self.name_zh is not None:
            names += " (%s)" % self.name_zh
        return names
    
    def email(self):
        if self.alt_email is None:
            return self.key().name()
        else:
            return self.alt_email
    
    def munging_google_account(self):
        return utils.munge_email(self.google_account())
    
    def munging_alt_email(self):
        return utils.munge_email(self.alt_email)
    
    def munging_email(self):
        return utils.munge_email(self.email())
    
    def ecole(self):
        return paristech.ECOLES.get(self.ecole_id)
    
    def university(self):
        return paristech.UNIVERSITIES.get(self.univ_id)
    
    def has_photo(self):
        return self.photo_type is not None and self.photo_data is not None
    
    def is_member(self):
        return AFCPUserProfile.MEMBER_ROLE in self.roles
    
    def is_editor(self):
        return AFCPUserProfile.EDITOR_ROLE in self.roles
    
    def add_editor(self):
        if AFCPUserProfile.EDITOR_ROLE not in self.roles:
            self.roles.append(AFCPUserProfile.EDITOR_ROLE)
    
    def count_login(self):
        self.last_login = datetime.datetime.utcnow()
        self.login_count += 1
    
    def put(self):
        # Set default value to login count.
        if self.login_count is None:
            self.login_count = 1
        # If the user is an AFCP member, add the member role. Otherwise, remove the member role.
        if self.roles is None:
            self.roles = []
        if self.ecole_id is not None:
            if AFCPUserProfile.MEMBER_ROLE not in self.roles:
                self.roles.append(AFCPUserProfile.MEMBER_ROLE)
        else:
            if AFCPUserProfile.MEMBER_ROLE in self.roles:
                self.roles.remove(AFCPUserProfile.MEMBER_ROLE)
        # Put the entity to datastore.
        return super(AFCPUserProfile, self).put()


#---------------------------------------------------------------------------------------------------
# AFCPUser: a wrapper around google.appengine.api.users.User
#---------------------------------------------------------------------------------------------------

class AFCPUser(object):

    def __init__(self, user):
        self._user = user
        
        if self._user:
            self._profile = AFCPUserProfile.get_by_key_name(self._user.email())
        else:
            self._profile = None
    
    def profile(self):
        return self._profile
    
    def google_user(self):
        return self._user
    
    def nickname(self):
        if self._profile:
            return self._profile.name
        elif self._user:
            return self._user.nickname()
        else:
            return None
    
    def email(self):
        if self._user:
            return self._user.email()
        else:
            return None
    
    def is_anonymous(self):
        return self._user is None
    
    def is_authenticated(self):
        return self._user is not None
    
    def __nonzero__(self):
        return self.is_authenticated()


def get_current_user():
    google_user = users.get_current_user()
    return AFCPUser(google_user)


def create_login_url(redirect_url):
    return users.create_login_url(redirect_url)


def create_logout_url(redirect_url):
    return users.create_logout_url(redirect_url)

#