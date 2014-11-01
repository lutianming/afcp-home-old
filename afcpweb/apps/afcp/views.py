#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Views for the afcp app.
#
# Created on 2008-10-28.
# $Id: views.py 41 2010-07-21 10:33:30Z guolin.mobi $
#

from afcpweb.apps.afcp import news_feed, planet, resources
from afcpweb.apps.afcp.config import Config
from afcpweb.apps.common import utils
from afcpweb.apps.common.actions import Language, get_common_data
from afcpweb.apps.misc.views import not_found
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.template import Context, loader
from google.appengine.api import mail
import datetime
import logging
import random
import urllib








def home(request):
    "Displays the AFCP home page."
    
    ctxt_dict = { "feeds"         : news_feed.FEEDS,
                  "banner_image"  : random.choice(resources.BANNER_IMAGES), 
                  }
    ctxt_dict.update(get_common_data(request))
    ctxt = Context(ctxt_dict)
    tmpl = loader.get_template("%s/home.html" % Config.APP_NAME)
    return HttpResponse(tmpl.render(ctxt))


def contact(request, lang=None):
    "Displays the requested static contact page in a requested or the current language."
    
    if lang is None:
        lang = Language.SUPPORTED_LANG_CODES
    if lang not in Language.SUPPORTED_LANG_CODES:
        lang = Language.DEFAULT_LANG_CODE
    
    ctxt_dict = { "page_name" : "contact",
                  "lang_code" :lang,}
    
    if request.method == 'POST':
        msg = sendMailToAfcp(request)
        if msg != '':
            ctxt_dict["errmsg"] = msg
        else:
            ctxt_dict["msgok"] = True
                
    ctxt_dict.update(get_common_data(request))
    ctxt = Context(ctxt_dict)
    tmpl = loader.get_template("%s/static/%s/contact/contact.html" % (Config.APP_NAME, lang ) )
    return HttpResponse(tmpl.render(ctxt))

def sendMailToAfcp(request):
    msg = request.POST.get('message', '')
    email = request.POST.get('email', '')
    fromArg = request.POST.get('from', '')
    if email == '' and msg == '':
        return u"Veuillez indiquer un e-mail auquel vous répondre et rédiger un message avant d'envoyer."
    if email == '':
        return u"Veuillez indiquer un e-mail auquel vous répondre."
    if msg == '':
        return u"Procédez dans l'ordre et Rédigez un message avant de l'envoyer :)"
    if fromArg == '':
        return u"Emplacement du formulaire sur le site non précisé."
    message = mail.EmailMessage(sender=u"AFCP <AFCParisTech@gmail.com>",
                        subject=u"Message envoyé par le formulaire de contact du site de l'AFCP, section %s" % fromArg)
    message.to = resources.contactus_emails
    message.reply_to = email
    message.body = u"Message envoyé par le formulaire de contact, par %s :\n%s" % (email, msg)
    message.send()
    return ''


def about(request, name=None, lang=None):
    "Displays the requested static about page in a requested or the current language."
    
    STATIC_PAGES = ( "nous", "paristech", "paristechchine" , "activities", "bureau")
    
    if name is None:
        name = "nous"
    if name not in STATIC_PAGES:
        not_found(request)
    
    if lang is None:
        lang = Language.get_lang(request)
    if lang not in Language.SUPPORTED_LANG_CODES:
        lang = Language.DEFAULT_LANG_CODE
        
    ctxt_dict = { "page_name"    : name,
                  "lang_code"    : lang, }
    ctxt_dict.update(get_common_data(request))
    ctxt = Context(ctxt_dict)
    tmpl = loader.get_template("%s/static/fr/about/%s.html" % (Config.APP_NAME, name ))
    return HttpResponse(tmpl.render(ctxt))


def news(request):
    "Displays the planet AFCP page (a feeds aggregator)."
    
    ctxt_dict = { "feeds"       : news_feed.FEEDS,
                  "page_name" : "news",
                  }
    ctxt_dict.update(get_common_data(request))
    ctxt = Context(ctxt_dict)
    tmpl = loader.get_template("%s/news.html" % Config.APP_NAME)
    return HttpResponse(tmpl.render(ctxt))


def afcpchine(request):
    "Displays the requested afcpchine page in a requested or the current language."
    return HttpResponseRedirect("/afcp/afcpchine/alumnisalon/")

def alumnisalon(request):
    "Displays the alumnisalon event details."
    return simplePage(request, "afcpchine", "alumnisalon")



def amusement(request):
    "Displays the requested amusement page in a requested or the current language."
    return HttpResponseRedirect("/afcp/amusement/bal/")
#     
#     if name is None:
#         name = "planet"
#     
#     if name == "planet":
#         return planet_afcp(request)
#     elif name == "photos":
#         return photos_afcp(request)
#     elif name == "lanternes":
#         return lanternes(request)
#     else:
#         return not_found(request)


def planet_afcp(request):
    "Displays the planet AFCP page (a feeds aggregator)."
    
    ctxt_dict = { "feeds"       : planet.FEEDS,
                  "page_name" : "planet",
                  }
    ctxt_dict.update(get_common_data(request))
    ctxt = Context(ctxt_dict)
    tmpl = loader.get_template("%s/amusement/planet.html" % Config.APP_NAME)
    return HttpResponse(tmpl.render(ctxt))


def photos_afcp(request):
    "Displays the photos AFCP page (a feeds aggregator)."
    
    ctxt_dict = { "feeds"       : planet.PHOTOS,
                  "page_name" : "photos",
                  }
    ctxt_dict.update(get_common_data(request))
    ctxt = Context(ctxt_dict)
    tmpl = loader.get_template("%s/amusement/photos.html" % Config.APP_NAME)
    return HttpResponse(tmpl.render(ctxt))


def lanternes(request):
    "Displays the 'fête des lanternes' page."
     
    ctxt_dict = { "page_name" : "lanternes",
                  }
    ctxt_dict.update(get_common_data(request))
    ctxt = Context(ctxt_dict)
    tmpl = loader.get_template("%s/amusement/lanternes.html" % Config.APP_NAME)
    return HttpResponse(tmpl.render(ctxt))

def gala(request):
    return simplePage(request, "amusement", "gala")

def bal(request):
    return simplePage(request, "amusement", "bal")

def research(request):
    "Displays the requested research page."
    return HttpResponseRedirect("/afcp/research/presentation/")

def presentation(request):
    "Displays the research presentation page."
    return simplePage(request, "research", "presentation")

def training(request):
    "Displays the training page."
    return simplePage(request, "research", "training")

def workpermit(request):
    "Displays the workpermit page."
    return simplePage(request, "research", "workpermit")
 
def misc(request):
    "Displays the requested miscellaneous page."
    return HttpResponseRedirect("/afcp/misc/nuitdechine/")

def itineraireX(request):
    "Displays the itinerary to go to X page."
    return simplePage(request, "misc", "itineraire-x")
#     
# #    if lang is None:
# #        lang = Language.get_lang(request)
# #    if lang not in Language.SUPPORTED_LANG_CODES:
# #        lang = Language.DEFAULT_LANG_CODE
#     
#     ctxt_dict = { "page_name" : "itineraire-x",
#                   }
#     ctxt_dict.update(get_common_data(request))
#     ctxt = Context(ctxt_dict)
#     tmpl = loader.get_template("%s/misc/itineraire-x.html" % Config.APP_NAME)
#     return HttpResponse(tmpl.render(ctxt))

def seminaire(request):
    "Displays the seminar event details."
    return simplePage(request, "misc", "seminaire")

def roundtable(request):
    "Displays the roundtable page."
    return simplePage(request, "misc", "roundtable")

def nuitdechine(request):
    "Displays the nuitdechine page."
    return simplePage(request, "misc", "nuitdechine")
#     
# #    if lang is None:
# #        lang = Language.get_lang(request)
# #    if lang not in Language.SUPPORTED_LANG_CODES:
# #        lang = Language.DEFAULT_LANG_CODE
#     
#     ctxt_dict = { "page_name" : "seminaire",
#                   }
#     ctxt_dict.update(get_common_data(request))
#     ctxt = Context(ctxt_dict)
#     tmpl = loader.get_template("%s/misc/seminaire.html" % Config.APP_NAME)
#     return HttpResponse(tmpl.render(ctxt))

def training_old(request):
    "Displays the training event details."
    #return simplePage(request, "misc", "training")
    return HttpResponsePermanentRedirect("/afcp/research/training/", )

def simplePage(request, category, name):
    
#    if lang is None:
#        lang = Language.get_lang(request)
#    if lang not in Language.SUPPORTED_LANG_CODES:
#        lang = Language.DEFAULT_LANG_CODE
    
    ctxt_dict = { "page_name" : name,
                  }
    ctxt_dict.update(get_common_data(request))
    ctxt = Context(ctxt_dict)
    tmpl = loader.get_template("%s/%s/%s.html" % (Config.APP_NAME, category, name))
    return HttpResponse(tmpl.render(ctxt))



#
