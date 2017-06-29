from .base import *

DEBUG = True

TEMPLATES[0]['OPTIONS']['loaders'] = [
  'django.template.loaders.filesystem.Loader',
  'django.template.loaders.app_directories.Loader'
]

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(SITE_ROOT, 'sent_emails')

INSTALLED_APPS += ('debug_toolbar',
           'django_nose',
           'crispy_forms')

MIDDLEWARE += (
  'debug_toolbar.middleware.DebugToolbarMiddleware',
)

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
    'rest_framework.authentication.SessionAuthentication',
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
