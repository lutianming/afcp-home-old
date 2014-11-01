#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Views for the Forum webapp.
#
# Created on 2008-10-28.
# $Id: views.py 41 2010-07-21 10:33:30Z guolin.mobi $
#


from afcpweb.apps.common import utils
from afcpweb.apps.forum import resources
from afcpweb.apps.forum.config import Config
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect,\
	HttpResponsePermanentRedirect
from django.template import Context, loader
from google.appengine.api import mail
from os.path import splitext
import datetime
import random

from google.appengine.ext import db
#from google.appengine.api import users







#---------------------------------------------------------------------------------------------------
# Home page, 404 not-found page, error page and static pages
#---------------------------------------------------------------------------------------------------

#defaultLanguage = "zh-cn"

def home(request, lang=None):
	"Display ths Forum home page."

	if lang is None:
		lang = "zh-cn"
		
	ctxt_dict = { "url" : request.path,
	              "lang_code" : lang,
	    	      "banner_image" : random.choice(resources.BANNER_IMAGES), }
				  
	ctxt = Context(ctxt_dict)
	tmpl = loader.get_template("%s/%s/home.html" % (Config.APP_NAME, lang) )
	return HttpResponse(tmpl.render(ctxt))
	
def visitor(request, name=None, lang=None):	
	"Display the Forum visitor page"
	
	supage_name = "visitors"
	if name is None:
		name = "program"

	if lang is None:
		lang = "zh-cn"
	
	ctxt_dict = { "supage_name": supage_name,
	              "page_name" : name,
	              "url" : request.path,
	              "lang_code"    : lang, 
	              "thispage" : "entry_" + supage_name + "_" + name }
	
	if name == "sendmail":
		if not sendmail(request):
			name = "nosendmail"
	
	if name == "applications":
		c = Candidate.all()
		results = c.fetch(100000)
		ctxt_dict["application"] = results
				  
	ctxt = Context(ctxt_dict)
	tmpl = loader.get_template("%s/%s/static/visitors/%s.html" % (Config.APP_NAME, lang, name) )
	return HttpResponse(tmpl.render(ctxt))

# Class used for google datastore (list of applications done)
class Candidate(db.Model):
    lastname = db.StringProperty(required=True)
    firstname = db.StringProperty(required=True)
    email = db.StringProperty(required=True)
    application_date = db.DateProperty(required=True)
    company = db.StringProperty(required=True)
    job = db.StringProperty(required=True)

def sendmail(request):
	if mail.is_email_valid(request.POST['email']):
		
		if (len(request.FILES) == 2 and len(request.POST) == 6):
			totalSize = 0
			for f in request.FILES.values():
				path, ext = splitext(f.name)
				totalSize += f.size
				if ext != '.doc' and ext != '.pdf':
					return False
			if totalSize > 1048576: # Max 1 Mo
				return False
			id = unicode(request.POST.get('id', ''))
			prenom = unicode(request.POST.get('prenom', '')).capitalize()
			nom = unicode(request.POST.get('nom', '')).upper()
			email = unicode(request.POST.get('email', ''))
			company = unicode(request.POST.get('company', ''))
			job = unicode(request.POST.get('jobname', ''))
			if (id == '' or prenom == '' or nom == '' or email == '' or company == '' or job == ''):
				return False
			
			message = mail.EmailMessage(sender=u"AFCP <AFCParisTech@gmail.com>",
	                            subject=u"%s : Nouvelle candidature envoyée par le site de l'AFCP" % job)
			
			message.to = unicode(resources.company_emails[id])
			message.cc = resources.application_cc
			
			
			message.body = u"""
Madame, Monsieur,

Une nouvelle candidature pour le poste %s a été envoyée par l'intermédiaire du site de l'AFCP, l'offre y étant publiée.

Veuillez trouver ci-joint le CV et la lettre de motivation de %s %s pour cette candidature. Vous pouvez le joindre à l'adresse e-mail %s

Bien à vous,

L'équipe AFCP
""" % (job, prenom, nom, email)

			message.html = u"""
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /></head><body><br/>
Madame, Monsieur,<br/>
<br/>
Une nouvelle candidature pour le poste %s a été envoyée par l'intermédiaire du site de l'AFCP, l'offre y étant publiée.<br/>
<br/>
Veuillez trouver ci-joint le CV et la lettre de motivation de %s %s pour cette candidature. Vous pouvez le joindre à l'adresse e-mail <a href="mailto:%s">%s</a>.<br/>
<br/>
Bien à vous,<br/>
<br/>
L'équipe AFCP<br/>
</body></html>
""" % (job, prenom, nom, email, email)

			
#			message.attachments = request.FILES.items()
			#message.attachments = [(filename + u"__" + replaceForbiddenCharacters(f.name), f.read()) for filename, f in request.FILES.items()]
			message.attachments = [(f.name, f.read()) for filename, f in request.FILES.items()]
			
		
			message.send()
			
			
			e = Candidate(lastname = nom,
						firstname = prenom,
						email = email,
						application_date = datetime.datetime.now().date(),
						company = company,
						job = job
						)
			e.put()
			
			return True
		else:
			return False
	else:
		return False

#def replaceForbiddenCharacters(s):
#	p = re.compile('(\\|\/|\:|\*|\?|\"|\<|\>|\|)')
#	return p.sub('_', s)


def exhibitor(request, name=None, lang=None):	
	"Display the Forum visitor page"
	
	supage_name = "exhibitors"
	
	if name is None:
		name = "visitors"  
	
	if lang is None:
		lang = "zh-cn"
	
	ctxt_dict = { "url" : request.path,
	              "lang_code"    : lang,	
	              "supage_name": supage_name,
	              "page_name" : name, 
	              "thispage" : "entry_" + supage_name + "_" + name}
	ctxt = Context(ctxt_dict)
	tmpl = loader.get_template("%s/%s/static/exhibitors/%s.html" % (Config.APP_NAME,  lang, name) )
	return HttpResponse(tmpl.render(ctxt))
	
	
def contact(request, name=None, lang=None):
	"Display the Forum contact page."
	
	if lang is None:
		lang = "zh-cn"
	
	if name is None:
		name = "contact"
		
	ctxt_dict = {"url" : request.path,
	             "lang_code" : lang,
	             "supage_name" : "contact",
	             "page_name" : name, 
	             "thispage" : "entry_contact_" + name}
	
	if name == "contact" and request.method == 'POST':
		msg = sendMailToAfcp(request)
		if msg != '':
			ctxt_dict["errmsg"] = msg
		else:
			ctxt_dict["msgok"] = True
					
	ctxt = Context(ctxt_dict)
	tmpl = loader.get_template("%s/%s/static/contact/%s.html" % (Config.APP_NAME, lang, name));
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
	message.body = u"Message envoyé par le formulaire de contact, par %s :\n\n%s" % (email, msg)
	message.send()
	return ''

def inscript(request, name=None, lang=None):
	"Display the Inscription Page."

	if lang is None:
		lang = "zh-cn"
	
	if name is None:
		name = "saint_gobain"

	ctxt_dict = {"url" : request.path,
	             "lang_code" : lang,
	             "supage_name" : "inscript",
	             "page_name" : name, 
	             "thispage" : "entry_inscript_" + name}
					
	ctxt = Context(ctxt_dict)
	tmpl = loader.get_template("%s/%s/static/inscription/%s.html" % (Config.APP_NAME, lang, name));
	return HttpResponse(tmpl.render(ctxt))

def saint_gobain(request, name=None, lang=None):
	"Display the Inscription Page."

	if lang is None:
		lang = "zh-cn"
	
	if name is None:
		name = "test"

	ctxt_dict = {"url" : request.path,
	             "lang_code" : lang,
	             "supage_name" : "inscript",
	             "page_name" : name, 
	             "thispage" : "entry_inscript_" + name}
					
	ctxt = Context(ctxt_dict)
	tmpl = loader.get_template("%s/%s/static/inscription/%s.html" % (Config.APP_NAME, lang, name));
	return HttpResponse(tmpl.render(ctxt))

def inscription(request, name=None, lang=None):
	"Display the Inscription Page."

	if lang is None:
		lang = "zh-cn"
	
	if name is None:
		name = "inscription"

	ctxt_dict = {"url" : request.path,
	             "lang_code" : lang,
	             "supage_name" : "inscript",
	             "page_name" : name, 
	             "thispage" : "entry_inscript_" + name}
					
	ctxt = Context(ctxt_dict)
	tmpl = loader.get_template("%s/%s/static/visitors/%s.html" % (Config.APP_NAME, lang, name));
	return HttpResponse(tmpl.render(ctxt))

def not_found(request):
	"Displays the 404 not-found page."
    
	ctxt_dict = { "url" : request.path, }
	ctxt = Context(ctxt_dict)
	tmpl = loader.get_template("%s/not_found.html" % Config.APP_NAME)
	return HttpResponseNotFound(tmpl.render(ctxt))

def redirect_to_new_website(request):
	return HttpResponsePermanentRedirect("http://www.forumhorizonchine.com")

