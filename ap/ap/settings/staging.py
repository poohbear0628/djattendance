from .base import *

import dj_database_url
import os

DEBUG = True

# Parse database configuration from $DATABASE_URL
DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

INSTALLED_APPS += (
    'debug_toolbar',
)

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',  # use local jquery (for offline development)
}

# Static asset configuration
BASE_DIR = os.path.dirname(os.path.abspath(__name__))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'ap/static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack/webpack-stats.json'),
    }
}

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
