from sentad.settings.common import *
import os

ALLOWED_HOSTS = ['api-pre.sentad.com', 'api.sentad.com']
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DEBUG = False

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
