#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Django settings for afcpweb project.
#
# Created on 2008-04-28
# $Id: settings.py 26 2009-08-04 22:06:00Z guolin.mobi $
#

import os

# If the webapp is deployed on localhost), set DEBUG to True; otherwise, set DEBUG to False.
DEPLOYED_ON_LOCALHOST = os.environ.get("SERVER_NAME", "").startswith("localhost")
# DEBUG = DEPLOYED_ON_LOCALHOST
DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

# Google App Engine does not support Django models:
# leave all DATABASE_* settings set to an empty string.
DATABASE_ENGINE   = ""
DATABASE_NAME     = ""
DATABASE_USER     = ""
DATABASE_PASSWORD = ""
DATABASE_HOST     = ""
DATABASE_PORT     = ""

# Local time zone for this installation. Choices can be found here:
#   http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "Europe/Paris"

# Language code for this installation. All choices can be found here:
#   http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
#   http://blogs.law.harvard.edu/tech/stories/storyReader$15
#LANGUAGE_CODE = "en-us"
LANGUAGE_CODE = "fr"

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ""

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = ""

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = "/media/"

# Make this unique, and don't share it with anybody.
SECRET_KEY = "*c(^-34)gdt8=g%3##=*apdl$!w8q-$4bc96+25!%2@%6-pj*q"

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.load_template_source",
    "django.template.loaders.app_directories.load_template_source",
    # 'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    
    "afcpweb.apps.middleware.sessions.SessionMiddleware",
    # "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "afcpweb.apps.middleware.common.LogErrorMiddleware",
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    "django.middleware.doc.XViewMiddleware",
)

ROOT_URLCONF = "afcpweb.urls"

ROOT_PATH = os.path.dirname(__file__)


TEMPLATE_DIRS = (os.path.normpath(os.path.join(os.path.dirname(__file__), "templates")),)

# For serving static files.
STATIC_DOC_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "static"))

INSTALLED_APPS = (
    "afcpweb",
    "afcpweb.apps",
    "afcpweb.apps.activities",
    "afcpweb.apps.afcp",
    "afcpweb.apps.admin",
    "afcpweb.apps.common",
    "afcpweb.apps.forum",
    "afcpweb.apps.members",    
    "afcpweb.apps.misc", 
    "afcpweb.apps.temps",   
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    # 'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.sites',
)


