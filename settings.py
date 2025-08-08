# -*- coding: utf-8 -*-

import os
PROJECT_ROOT_PATH = os.path.realpath(os.path.dirname(__file__))

DEBUG = True
#DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS
"""
DATABASE_ENGINE = 'mysql'
DATABASE_NAME = 'sgs'
DATABASE_USER = 'root'
DATABASE_PASSWORD = '6pxh2u2c'
DATABASE_HOST = 'localhost'
DATABASE_PORT = '3306'
"""
DATABASE_ENGINE = 'mysql'
DATABASE_NAME = 'sgs'
DATABASE_USER = 'frontend'
DATABASE_PASSWORD = 'sgs123'
DATABASE_HOST = '146.134.250.208'
DATABASE_PORT = '3306'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Sao_Paulo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pt-br'
LANGUAGES = (
    ('pt-br', u'Português'),
    ('en', u'Inglês'),
    ('es', u'Espanhol'),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

try:
    from local_settings import *
except:
    pass

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
#MEDIA_ROOT = ''
MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin-media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'quam-f!+0rtxe!l038e8avh-5p=8d2aqb@#r1%ltc@i&%0((7e'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
#    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates"
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    MEDIA_ROOT + '/templates',
    os.path.join(PROJECT_ROOT_PATH, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    #'tags.context.context_processors',
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',

    #relatórios
    'hosts',

    #usr
    'usr',

    #gerência
    'gerencia.latencia',
    'gerencia.estacaodetrabalho',
    'gerencia.hosts2',
    'gerencia.instituicao',
    'gerencia.redes',
    'gerencia.snmp',
    'gerencia.usr',

)
