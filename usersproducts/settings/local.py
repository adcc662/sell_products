from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ecommerce',
        'USER': 'user',
        'PASSWORD': 'u%(&)A4n/',
        'HOST': 'db',
        'PORT': 5432,
    }
}

STATIC_URL = 'static/'
DEBUG = True

ALLOWED_HOSTS = []
