from sentad.settings.common import *
import os


ALLOWED_HOSTS = ['*']
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['RDS_DB_NAME'],
        'USER': "ebroot",
        'PASSWORD': "Fousiane0",
        'HOST': os.environ['RDS_HOSTNAME'],
        'PORT': os.environ['RDS_PORT'],
    }
}