import os
from common import *

###### START DEBUG CONFIGURATION ######
DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['.veskoy.com']
###### END DEBUG CONFIGURATION ######

###### START EMAIL CONFIGURATION ######
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
CONTACT_EMAIL = 'admin@veskoy.com'
###### END EMAIL CONFIGURATION ######

###### START DATABASE CONFIGURATION ######
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': 3306
    }
}
###### END DATABASE CONFIGURATION ######

###### START CACHE CONFIGURATION ######
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': normpath(join(ENV_ROOT, 'project_cache')),
        'TIMEOUT': 10*60, # 10 minutes
    }
}
###### END CACHE CONFIGURATION ######