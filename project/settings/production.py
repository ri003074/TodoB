import django_heroku
from .base import *  # noqa

DEBUG = False

django_heroku.settings(locals())
