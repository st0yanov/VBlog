from os.path import abspath, basename, dirname, join, normpath
from sys import path

###### START PATH CONFIGURATION ######
# abspath(__file__) - .../VBlog/VBlog/settings/common.py
# dirname(dirname(abspath(__file__))) - .../VBlog/VBlog/settings
# dirname(dirname(dirname(abspath(__file__)))) - .../VBlog/VBlog - Django Root directory
DJANGO_ROOT = dirname(dirname(dirname(abspath(__file__))))

# Project Name
PROJECT_NAME = basename(DJANGO_ROOT)

# dirname(DJANGO_ROOT) - .../VBlog - The path to the environment
ENV_ROOT = dirname(DJANGO_ROOT)

# The file that holds the value for the SECRET_KEY variable
SECRET_FILE = normpath(join(ENV_ROOT, 'deploy', 'SECRET'))
###### END PATH CONFIGURATION ######

###### START DEBUG CONFIGURATION ######
DEBUG = False
TEMPLATE_DEBUG = False
###### END DEBUG CONFIGURATION ######

###### START MANAGER CONFIGURATION ######
ADMINS = (
    ('Vesko', 'admin@veskoy.com'),
)

MANAGERS = ADMINS
###### END MANAGER CONFIGURATION ######

###### START GENERAL CONFIGURATION ######
TIME_ZONE = 'Europe/Sofia'
LANGUAGE_CODE = 'bg-bg'
USE_I18N = True
USE_L10N = True
USE_TZ = True
###### END GENERAL CONFIGURATION ######

###### START MEDIA CONFIGURATION ######
MEDIA_ROOT = normpath(join(DJANGO_ROOT, 'media'))
MEDIA_URL = '/media/'

CKEDITOR_UPLOAD_PATH = 'uploads/'
###### END MEDIA CONFIGURATION ######

###### START STATIC CONFIGURATION ######
STATIC_ROOT = normpath(join(DJANGO_ROOT, 'static'))
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

"""
STATICFILES_DIRS = (
    normpath(join(DJANGO_ROOT, 'assets'))
)
"""
###### END STATIC CONFIGURATION ######

###### START TEMPLATE CONFIGURATION ######
TEMPLATE_DIRS = (
    normpath(join(DJANGO_ROOT, 'templates')),
)
###### END TEMPLATE CONFIGURATION ######
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
###### END MIDDLEWARE CONFIGURATION ####

###### START APPS CONFIGURATION ######
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Admin Panel
    'django.contrib.admin',

    # Database migrations
    'south',

    # Full-text search
    'whoosh',
    'haystack',

    # WYSIWYG editor field
    'ckeditor',

    # Auto Slug Generator
    'autoslug',

    # CAPTCHA field
    'captcha',

    # The main Blog App
    'Apps.Blog',
)
###### END APPS CONFIGURATION ######

###### START URL CONFIGURATION ######
ROOT_URLCONF = '%s.urls' % PROJECT_NAME
###### END URL CONFIGURATION ######

###### START WSGI CONFIGURATION ######
WSGI_APPLICATION = '%s.wsgi.application' % PROJECT_NAME
###### END WSGI CONFIGURATION ######

###### START WHOOSH CONFIGURATION ######
WHOOSH_INDEX = normpath(join(ENV_ROOT, 'whoosh'))
###### END WHOOSH CONFIGURATION ######

###### START HAYSTACK CONFIGURATION ######
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': WHOOSH_INDEX,
    },
}
###### END HAYSTACK CONFIGURATION ######

###### START SECRET_KEY CONFIGURATION ######
try:
    SECRET_KEY = open(SECRET_FILE).read().strip()
except IOError:
    try:
        with open(SECRET_FILE, 'w+') as f:
            import random
            SECRET_KEY = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
            f.write(SECRET_KEY)
    except IOError:
        raise Exception('Cannot open %s file for writing.' % SECRET_FILE)
###### END SECRET_KEY CONFIGURATION ######