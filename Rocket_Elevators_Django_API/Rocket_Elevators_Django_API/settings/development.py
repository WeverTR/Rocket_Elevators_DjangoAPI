# Python imports
from os.path import join

# project imports
from .common import *
from pathlib import Path
import os
import environ

# uncomment the following line to include i18n
# from .i18n import *

# Initialise environment variablesenv = environ.Env()environ.Env.read_env()
env = environ.Env()
environ.Env.read_env()

# ##### DEBUG CONFIGURATION ###############################
DEBUG = True

# allow all hosts during development
ALLOWED_HOSTS = ['*']

# ##### DATABASE CONFIGURATION ############################
DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PW'),
        'HOST': env('DATABASE_HOST'),
        'PORT': '3306',
        'OPTIONS': {
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
                }
        }
 }

# ##### APPLICATION CONFIGURATION #########################

INSTALLED_APPS = DEFAULT_APPS
