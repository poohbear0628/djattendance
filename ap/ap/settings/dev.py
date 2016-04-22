from .base import *

DEBUG = True
TEMPLATE_DEBUG = True

INSTALLED_APPS += ('autofixture',
                   # 'debug_toolbar',
                   'django_nose',
                   'anonymizer',
                   'crispy_forms')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djattendance',
        'USER': 'ap',
        'PASSWORD': '4livingcreatures',
        'HOST': 'localhost',
        'PORT': '',
    }
}
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
    ),
   'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

INTERNAL_IPS = ('127.0.0.1',)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',  # use local jquery (for offline development)
}

