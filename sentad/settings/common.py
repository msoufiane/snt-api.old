import os

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '_hjyk)x4n1427a6@m6@l#fo+!6r9%x1ptng+10ie()70mabj70')

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.auth',
    'django_extensions',

    'raven.contrib.django.raven_compat',
    'rest_framework',
    'corsheaders',
    'knox',

    'authentication',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

CORS_ORIGIN_ALLOW_ALL = True
AUTH_USER_MODEL = 'authentication.Account'
WSGI_APPLICATION = 'sentad.wsgi.application'
ROOT_URLCONF = 'sentad.urls'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
