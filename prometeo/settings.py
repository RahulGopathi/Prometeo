"""
Django settings for prometeo project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', cast=str)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['prometeo.iitj.ac.in', '192.168.43.110', '127.0.0.1', '142.93.216.166', 'dev.prometeo.in', 'prometeo.in', 'www.prometeo.in', 'localhost']


# Application definition

INSTALLED_APPS = [
    'home',
    'events',
    'coordinator',
    'users',
    'dashboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.facebook',
    'crispy_forms',
    'widget_tweaks',
    'django_inlinecss',

    'captcha'
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'prometeo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'prometeo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

if config('SQLITE_DB', cast=bool):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': config('DB_HOST', default='localhost'),
            'PORT': config('DB_PORT', cast=int, default=5432),
        }
    }

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'prometeo/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# email config
DEFAULT_FROM_EMAIL = config('SERVER_EMAIL', cast=str)

EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_PORT = config('SERVER_EMAIL_PORT', cast=int, default=587)
EMAIL_HOST = config('SERVER_EMAIL_HOST', cast=str, default="smtp.zoho.in")
EMAIL_HOST_USER = config('SERVER_EMAIL', cast=str)
EMAIL_HOST_PASSWORD = config('SERVER_EMAIL_PASSWORD', cast=str)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EVENTS_MAIL_RECEPIENTS = config('EVENTS_MAIL_RECEPIENTS', cast=str)

AUTH_USER_MODEL = 'users.CustomUser'

# django-allauth registraion settings
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 0.25
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5

ACCOUNT_USER_MODEL_EMAIL_FIELD = 'email'
# ACCOUNT_USER_MODEL_USERNAME_FIELD = 'email'
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_EMAIL_REQUIRED = True
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_UNIQUE_EMAIL = True


LOGIN_REDIRECT_URL = "/"

ACCOUNT_FORMS = {
    'signup': 'users.forms.SignUpForm',
    'login': 'users.forms.CustomLoginForm'
}

ACCOUNT_ADAPTER = 'prometeo.account_adapter.NoNewUsersAccountAdapter'

RECAPTCHA_PUBLIC_KEY = config('RECAPTCHA_PUBLIC_KEY', cast=str)
RECAPTCHA_PRIVATE_KEY = config('RECAPTCHA_PRIVATE_KEY', cast=str)
RECAPTCHA_USE_SSL = config('RECAPTCHA_USE_SSL', cast=str, default=True)


ADMINS = [('Aryan', 'garg.10@iitj.ac.in'), ('Sahil', 'santosh.2@iitj.ac.in'), ('Rahul', 'gopathi.1@iitj.ac.in'), ('Sainath', 'reddy.17@iitj.ac.in'), ('Shrutayu', 'aggarwal.4@iitj.ac.in'), ('Joel', 'thomas.2@iitj.ac.in'),]
MANAGERS = ADMINS