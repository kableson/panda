from .base import *

DEBUG = False
ADMINS = (
    ('educaproject.com', 'www.educaproject.com',)
)

ALLOWED_HOSTS = ['.educaproject.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': '147258',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
