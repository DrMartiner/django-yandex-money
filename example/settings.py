# -*- coding: utf-8 -*-

import sys
import os.path

try:
    from settings_local import *
except ImportError:
    print "Don't forget create settings_local.py"

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, '..'))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SECRET_KEY = 'SECRET_KEY'
ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'example/templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.static',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'app',
    'south',
    'yandex_money',
)

YANDEX_MONEY_SCID = 123
YANDEX_MONEY_SHOP_ID = 456
YANDEX_MONEY_SHOP_PASSWORD = 'password'
YANDEX_MONEY_DEBUG = DEBUG
YANDEX_MONEY_FAIL_URL = 'http://example.com/fail-payment/'
YANDEX_MONEY_SUCCESS_URL = 'http://example.com/success-payment/'

try:
    from settings_local import *
except ImportError:
    pass