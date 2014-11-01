#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created on 2010-02-05.
# $Id: main.py 41 2010-07-21 10:33:30Z guolin.mobi $
#

"""Bootstrap script for running a Django application on Google App Engine.
"""

#---------------------------------------------------------------------------------------------------

# Must set these environment variables before importing any part of Django.
#import os
#os.environ["DJANGO_SETTINGS_MODULE"] = "afcpweb.settings"

# Select Django version.
#import google.appengine.dist
#google.appengine.dist.use_library("django", "1.2")

# Force Django to reload its settings.
#import django.conf
#django.conf.settings._target = None

# Django imports.
import django.core.handlers.wsgi
import django.core.signals
import django.db
import django.dispatch.dispatcher


#---------------------------------------------------------------------------------------------------

import logging

# Log exceptions.
def log_exception(*args, **kwds):
    logging.exception("Exception in request:")

# Update Django signal listeners.
django.core.signals.got_request_exception.disconnect(django.db._rollback_on_exception)
django.core.signals.got_request_exception.connect(log_exception)

#---------------------------------------------------------------------------------------------------


# Create a Django application for WSGI.
app = django.core.handlers.wsgi.WSGIHandler()

# Old method with Python 2.5 :

# def main():
#     # Create a Django application for WSGI.
#     app = django.core.handlers.wsgi.WSGIHandler()
#     # Run the WSGI CGI handler with that application.
#     google.appengine.ext.webapp.util.run_wsgi_app(app)
# 
# if __name__ == "__main__":
#     main()


