from .base import *

DEBUG = True

# Database
DATABASES['default'].update({
    'USER': 'blog',
    'PASSWORD': 'blog',
    'HOST': '127.0.0.1',
})

# Django debug toolbar settings
INSTALLED_APPS += [
    'debug_toolbar',
]
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
INTERNAL_IPS = [
    '127.0.0.1',
]
