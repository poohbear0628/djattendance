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
  'SHOW_TEMPLATE_CONTEXT': True,
}

# Communicating with firewall for granting web access requests
HOST = "10.0.8.20" # hostname or ip address of the firewall (add to /etc/hosts)
PORT = 12345 # server port of application which listens for commands on the firewall

# Logging for import module is set up to create a new log file at midnight, and renames the
# old file to include the date that it was created.  Django runs with two processes, a parent
# process that spawns the server as a child process each time a change is detected.  We can't
# roll over (rename the original log file) since the parent process is holding on to a handle
# to the log file.  So the purpose of these two lines is to not let the parent process hold
# on to a handle to any log files, yay!
if DEBUG and os.environ.get('RUN_MAIN', None) != 'true':
  LOGGING = {}
