from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z@2kayk-07efjgp5ge@+^u6_p21rf1u-9(_a%%n1awd8j4(ils'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'woyd',
        'USER': 'woyd',
        'PASSWORD': 'woyd',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
