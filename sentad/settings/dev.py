from sentad.settings import common as common_settings
from sentad.settings.common import *
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATIC_URL = '/static/'
STATIC_ROOT = 'static/'
ALLOWED_HOSTS = ['*']
DEBUG = True

INSTALLED_APPS = common_settings.INSTALLED_APPS + [
    'django.contrib.staticfiles',
    'django_extensions',
]

REST_FRAMEWORK = {
    'UNAUTHENTICATED_USER': None,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'page_size_query_param': 'page_size',
    'max_page_size': 10000,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': ('knox.auth.TokenAuthentication',),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
