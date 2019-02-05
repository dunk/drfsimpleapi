from __future__ import absolute_import, unicode_literals

from .base import *

INSTALLED_APPS.append('rest_framework')
INSTALLED_APPS.append('simpleapi')

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.postgresql',
      'HOST': 'happydb',
      'NAME': 'simpleapi',
      'USER': 'postgres',
      'PASSWORD': 'mypassword',
  },
}

SECRET_KEY = '1zetIbhaWApm'
