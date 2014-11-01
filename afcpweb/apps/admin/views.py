#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Views for the admin app.
#
# Created on 2008-10-28.
# $Id: views.py 40 2010-03-08 23:05:09Z guolin.mobi $
#

import urllib
import logging
import datetime

from django.template import loader
from django.template import Context
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from afcpweb.apps.common import utils
from afcpweb.apps.common.actions import get_common_data
from afcpweb.apps.members.models import get_current_user


from afcpweb.apps.admin.access import AdminAccess
from afcpweb.apps.admin.config import Config

from afcpweb.apps.activities.models import AFCPActivity


def admin(request):
    return view_all_activity(request)

def get_activity_data(request):
    ctxt_dict = { "page_name"    : "activity",}
    ctxt_dict.update(get_common_data(request))
    return ctxt_dict
    
def view_all_activity(request):
    "Displays the admin console and handles the admin request."
    
    user = get_current_user()
    access = AdminAccess(user)
    if not access.can_consult:
        return HttpResponseRedirect("/afcp/")
    
    error = utils.get_param(request.GET, "error")
    info  = utils.get_param(request.GET, "info" )
        
    ACTIVITY_PER_PAGE = 8
    #query = AFCPActivity.gql("")
    query = AFCPActivity.find_all()
    page_number = utils.get_param(request.REQUEST, "page")
    activities = utils.EntityPage(query, ACTIVITY_PER_PAGE, page_number)
        
    ctxt_dict = { "info"         : info, 
                  "error"        : error, 
                  "activities"   : activities, 
                  "has_previous" : activities.has_previous(),
                  "has_next"     : activities.has_next(), 
                  "previous_page": activities.previous_page_number(),
                  "next_page"    : activities.next_page_number(),}
                     
    ctxt_dict.update(get_activity_data(request))
    ctxt = Context(ctxt_dict)
    tmpl = loader.get_template("%s/admin_activities.html" % Config.APP_NAME)
    return HttpResponse(tmpl.render(ctxt))


def create_activity(request, uid=None):

    activity = AFCPActivity.get_unique(uid)
    if request.method == "GET":
        if activity is None:
            isUpdateMode = False
        else :    
            isUpdateMode = True
        
        # enter the information
        ctxt_dict = { "isUpdateMode"  : isUpdateMode,
                      "info"          : utils.get_param(request.GET, "info"),
                      "error"         : utils.get_param(request.GET, "error"),
                      "activity"      : activity,}
                      
        ctxt_dict.update(get_activity_data(request))
        ctxt = Context(ctxt_dict)
        tmpl = loader.get_template("%s/activity/create_activity.html" % Config.APP_NAME)
        return HttpResponse(tmpl.render(ctxt))
    
    elif request.method == "POST":
        # Create an activity for the current user.
        try:
            date_str =  utils.get_param(request.POST, "date")
            if date_str is not None:
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
            else:
                date = None

            if uid is None: 
                uid = utils.generate_random_id("U")
                name = utils.get_param(request.POST, "name")
                subject = utils.get_param(request.POST, "subject")
                address = utils.get_param(request.POST, "address")
                spreadsheet_link = utils.get_param(request.POST, "spreadsheet_link")

                activity = AFCPActivity( uid=uid,
                                         name=name,
                                         subject=subject,
                                         address=address,
                                         spreadsheet_link=spreadsheet_link,
                                         date= date,
                                         is_closed = "no" )        
            else:
                activity = AFCPActivity.get_unique(uid)
                activity.name = utils.get_param(request.POST, "name")
                activity.subject = utils.get_param(request.POST, "subject")
                activity.address = utils.get_param(request.POST, "address")
                activity.spreadsheet_link = utils.get_param(request.POST, "spreadsheet_link")
                activity.is_closed = utils.get_param(request.POST, "is_closed")
                activity.date = date
                
            activity.put()
            
            ctxt_dict = { "info"          : utils.get_param(request.GET, "info"),
                          "error"         : utils.get_param(request.GET, "error"),
                          "activity"      : activity,}
                      
            ctxt_dict.update(get_common_data(request))
            ctxt = Context(ctxt_dict)
            tmpl = loader.get_template("%s/activity/view_activity.html" % Config.APP_NAME)
            return HttpResponse(tmpl.render(ctxt))
        except Exception, ex:
            error = "Failed to create an activity: %s" % str(ex)
            logging.error(error)
            params = { "error" : error,
                       "activity" : activity, }
            return HttpResponseRedirect("%s?%s" % (request.path, urllib.urlencode(params)))


def view_activity(request,uid):

    activity = AFCPActivity.get_unique(uid)
    if request.method == "GET":        
        ctxt_dict = { "info"          : utils.get_param(request.GET, "info"),
                      "error"         : utils.get_param(request.GET, "error"),
                      "activity"      : activity,}
                          
        ctxt_dict.update(get_activity_data(request))
        ctxt = Context(ctxt_dict)
        tmpl = loader.get_template("%s/activity/view_activity.html" % Config.APP_NAME)
        return HttpResponse(tmpl.render(ctxt))
    else :
        return not_found(request)

def delete_activity(request, uid):

    activity = AFCPActivity.get_unique(uid)
    if request.method == "GET":        
        ctxt_dict = { "info"          : utils.get_param(request.GET, "info"),
                      "error"         : utils.get_param(request.GET, "error"),
                      "activity"      : activity,}
                          
        ctxt_dict.update(get_activity_data(request))
        ctxt = Context(ctxt_dict)
        tmpl = loader.get_template("%s/activity/delete_activity.html" % Config.APP_NAME)
        return HttpResponse(tmpl.render(ctxt))
    elif request.method == "POST":
        activity.delete()
        info = "Success to delete activity." 
        logging.info(info)
        params = { "info" : info, }
        return HttpResponseRedirect("/admin/activity/?%s" % urllib.urlencode(params) )    
               

#