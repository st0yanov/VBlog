import os
from common import *

###### START DEBUG CONFIGURATION ######
DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']
###### END DEBUG CONFIGURATION ######

###### START EMAIL CONFIGURATION ######
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
CONTACT_EMAIL = 'root@localhost'
###### END EMAIL CONFIGURATION ######

###### START DATABASE CONFIGURATION ######
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': normpath(join(ENV_ROOT, 'db', 'default.sqlite3')),
    }
}
###### END DATABASE CONFIGURATION ######

###### START CACHE CONFIGURATION ######
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
###### END CACHE CONFIGURATION ######