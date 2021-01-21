import django_heroku
from .base import *  # noqa

DEBUG = True  # should be false but for debug

django_heroku.settings(locals())
