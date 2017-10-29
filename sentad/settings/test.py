from sentad.settings.common import *
from datetime import timedelta

ALLOWED_HOSTS = ['*']
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sentadtest',
        'USER': 'sentadtest',
        'PASSWORD': '59G1M%S32gHg',
        'HOST': '79.143.182.137',
        'PORT': '5432',
    }
}


REST_FRAMEWORK = {
    'UNAUTHENTICATED_USER': None,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'page_size_query_param': 'page_size',
    'max_page_size': 10000,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': ('knox.auth.TokenAuthentication',),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}

REST_KNOX = {
  'SECURE_HASH_ALGORITHM': 'cryptography.hazmat.primitives.hashes.MD5',
  'AUTH_TOKEN_CHARACTER_LENGTH': 64,
  'TOKEN_TTL': timedelta(hours=10),
  'USER_SERIALIZER': 'knox.serializers.UserSerializer',
}

