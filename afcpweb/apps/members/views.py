#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Views for the members app.
#
# Created on 2008-10-28.
# $Id: views.py 40 2010-03-08 23:05:09Z guolin.mobi $
#

import logging
import urllib

from django.template import loader
from django.template import Context
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from afcpweb.apps.common.actions import get_common_data
from afcpweb.apps.common import utils

from afcpweb.apps.members.config import Config
from afcpweb.apps.members import paristech

from afcpweb.apps.members.models import get_current_user
from afcpweb.apps.members.models import AFCPUserProfile


def view_members(request):
    """Displays the AFCP members list."""
    
    MEMBERS_PER_PAGE = 10
    query = AFCPUserProfile.gql("WHERE deleted=:deleted ORDER BY name", deleted=False)
    page_number = utils.get_param(request.REQUEST, "page")
    members = utils.EntityPage(query, MEMBERS_PER_PAGE, page_number)
   
    ctxt_dict = { "members"      : members, 
                  "has_previous" : members.has_previous(),
                  "has_next"     : members.has_next(), 
                  "previous_page" : members.previous_page_number(),
                  "next_page"    : members.next_page_number(),}
                  
    ctxt_dict.update(get_common_data(request))
    ctxt = Context(ctxt_dict)
    tmpl = loader.get_template("%s/members.html" % Config.APP_NAME)
    return HttpResponse(tmpl.render(ctxt))


def my_profile(request):
    """If current user already has a profile, redirect to the profile page; otherwise, display the
    create profile page.
    """
    
    # Anonymous user should not have arrived to this page.
    user = get_current_user()
    if not user:
        return HttpResponseRedirect("%s/" % Config.URL_PREFIX)
    
    # If the user already has a profile, redirect to the profile page.
    if user.profile() is not None:
        return HttpResponseRedirect("%s/profile/%s/" % (Config.URL_PREFIX, user.profile().uid))
    
    # Create profile for the current user.
    if request.method == "GET":
        # Return the create profile form.
        ctxt_dict = { "error"        : utils.get_param(request.GET, "error"),
                      "ecoles"       : paristech.ECOLES.values(),
                      "universities" : paristech.UNIVERSITIES.values(), }
        ctxt_dict.update(get_common_data(request))
        ctxt = Context(ctxt_dict)
        tmpl = loader.get_template("%s/create_profile.html" % Config.APP_NAME)
        return HttpResponse(tmpl.render(ctxt))
    
    elif request.method == "POST":
        # Create a profile for the current user.
        try:
            key_name = user.email()
            logging.info(key_name)
            uid = utils.generate_random_id("U")
            logging.info(uid)
            name = utils.get_param(request.POST, "name")
            logging.info(name)
            name_zh = utils.get_param(request.POST, "name_zh")
            logging.info(name_zh)
            status = AFCPUserProfile.PENDING_STATUS
            profile = AFCPUserProfile( key_name=key_name,
                                       uid=uid,
                                       name=name,
                                       name_zh=name_zh,
                                       status=status )
            profile.put()
            return HttpResponseRedirect("%s/profile/%s/" % (Config.URL_PREFIX, profile.uid))
        except Exception, ex:
            error = "Failed to create user profile: %s" % str(ex)
            logging.error(error)
            params = { "error" : error, }
            return HttpResponseRedirect("%s?%s" % (request.path, urllib.urlencode(params)))


def profile(request, uid):
    """Displays the member profile by UID."""
    
    profile = AFCPUserProfile.gql("WHERE uid=:uid", uid=uid).get()
    if profile is None:
        return not_found(request)
    
    if request.method == "GET":
        ctxt_dict = { "info"         : utils.get_param(request.GET, "info"),
                      "error"        : utils.get_param(request.GET, "error"),
                      "uid"          : uid,
                      "profile"      : profile,
                      "ecoles"       : paristech.ECOLES.values(),
                      "universities" : paristech.UNIVERSITIES.values(), }
        ctxt_dict.update(get_common_data(request))
        ctxt = Context(ctxt_dict)
        tmpl = loader.get_template("%s/profile.html" % Config.APP_NAME)
        return HttpResponse(tmpl.render(ctxt))
    
    elif request.method == "POST":
    
        params = {}
        action = utils.get_param(request.POST, "action")
        try:
            if action == "edit":
                # Update basic information.
                profile.name = utils.get_param(request.POST, "name")
                profile.name_zh = utils.get_param(request.POST, "name_zh")
                profile.sex = utils.get_param(request.POST, "sex")
                birthday_str = utils.get_param(request.POST, "birthday")
                if birthday_str is not None:
                    profile.birthday = datetime.datetime.strptime(birthday_str, "%Y-%m-%d")
                else:
                    profile.birthday = None
                promo_str = utils.get_param(request.POST, "promo")
                if promo_str is not None:
                    profile.promo = int(promo_str)
                else:
                    profile.promo = None
                profile.ecole_id = utils.get_param(request.POST, "ecole_id")
                profile.univ_id = utils.get_param(request.POST, "univ_id")
                profile.alt_email = utils.get_param(request.POST, "alt_email")
                profile.tel = utils.get_param(request.POST, "tel")
                
                # Update profile photo.
                """
                query_dict = request.POST.copy()
                query_dict.update(request.FILES)
                photo_dict = query_dict.get("photo", None)
                if photo_dict is not None:
                    profile.photo_type = utils.get_param(photo_dict, "content-type")
                    profile.photo_data = photo_dict.get("content")
                elif utils.get_param(request.POST, "delete_photo") == "1":
                    profile.photo_type = None
                    profile.photo_data = None
                """
                # Update profile in datastore.
                profile.put()
                params["info"] = "Profile updated successfully."
            
            elif action == "delete":
                profile.deleted = True
                profile.put()
                params["info"] = "Profile deleted successfully."
            
            elif action == "restore":
                profile.deleted = False
                profile.put()
                params["info"] = "Profile restored successfully."
            
            else:
                raise Exception, "Unknown action '%s'." % action
        
        except Exception, ex:
            error = "Failed to perform action '%s': %s" % (action, str(ex))
            logging.error(error)
            params["error"] = error
        
        return HttpResponseRedirect("%s?%s" % (request.path, urllib.urlencode(params)))


def profile_photo(request, uid):
    
    profile = AFCPUserProfile.gql("WHERE uid=:uid", uid=uid).get()
    if profile is None:
        return not_found(request)
    
    if request.method == "GET":
        if profile.has_photo():
            return HttpResponse(profile.photo_data, mimetype=profile.photo_type)
        else:
            return not_found(request)


def random_profile(request):
    # TODO: count() and fetch() cannot handle a large amount of results.
    # This function should be redesigned to be more scalable.
    query = AFCPUserProfile.gql("")
    count = query.count()
    if count <= 0:
        return not_found(request)
    
    random_offset = random.choice(range(0, count))
    profile_list  = query.fetch(1, random_offset)
    if not profile_list:
        return not_found(request)
    else:
        profile_uid = profile_list[0].uid
        return HttpResponseRedirect("%s/profile/%s/" % (Config.URL_PREFIX, profile_uid))        


#---------------------------------------------------------------------------------------------------


def ecole(request, acronym):

    if request.method == "GET":
        MEMBERS_PER_PAGE = 20
        query = AFCPUserProfile.gql( "WHERE ecole_id=:acronym AND deleted=:deleted ORDER BY name",
                                     acronym=acronym,
                                     deleted=False )
        page_number = utils.get_param(request.REQUEST, "page")
        members = utils.EntityPage(query, MEMBERS_PER_PAGE, page_number)
        ctxt_dict = { "members" : members,
                      "ecole"   : paristech.ECOLES.get(acronym),
                      "ecoles"  : paristech.ECOLES.values(), }
        ctxt_dict.update(get_common_data(request))
        ctxt = Context(ctxt_dict)
        tmpl = loader.get_template("%s/ecole.html" % Config.APP_NAME)
        return HttpResponse(tmpl.render(ctxt))


def university(request, acronym):

    if request.method == "GET":
        MEMBERS_PER_PAGE = 20
        query = AFCPUserProfile.gql( "WHERE univ_id=:acronym AND deleted=:deleted ORDER BY name",
                                     acronym=acronym,
                                     deleted=False )
        page_number = utils.get_param(request.REQUEST, "page")
        members = utils.EntityPage(query, MEMBERS_PER_PAGE, page_number)
        ctxt_dict = { "members"      : members,
                      "university"   : paristech.UNIVERSITIES.get(acronym),
                      "universities" : paristech.UNIVERSITIES.values(), }
        ctxt_dict.update(get_common_data(request))
        ctxt = Context(ctxt_dict)
        tmpl = loader.get_template("%s/university.html" % Config.APP_NAME)
        return HttpResponse(tmpl.render(ctxt))    


#