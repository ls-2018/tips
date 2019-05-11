# _*_coding:utf-8_*_
"""
Django settings for CrazyEye project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, datetime
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'suv(+n%(x)z-d*e82vrhqgxxzx@)s%ke-)v527mx0d@x4ii1y3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    # 'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'web',
    'bernard',
    'session_security',
    'kingadmin',
    'django_celery_beat',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'session_security.middleware.SessionSecurityMiddleware',
)

ROOT_URLCONF = 'CrazyEye.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["%s/%s" % (BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'django.core.context_processors.request',

            ],
        },
    },
]

WSGI_APPLICATION = 'CrazyEye.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'CrazyEyes',
#         'HOST': '',
#         'PORT':3306,
#         'USER':'root',
#         'PASSWORD': 'alex3714'
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'crazyeye_db',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'Asia/Shanghai'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    "%s/%s" % (BASE_DIR, "statics"),
]

AUTH_USER_MODEL = 'web.UserProfile'

LOGIN_URL = '/login/'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

MaxTaskProcesses = 4
MultiTaskScript = '%s/%s' % (BASE_DIR, 'backend/multitask_old.py')

RSA_PRIVATE_KEY_FILE = '%s/%s' % (BASE_DIR, 'var/rsa_key/id_rsa')

Welcome_msg = '''
|-------\033[32;1m[Welcome login CrazyEye Auditing System]\033[0m-----|
|            Version :   1.0                         |
|            Author  :   xxxxxx                    |
|            QQ Group:   29215534                    |
|----------------------------------------------------|\n\n'''

FileUploadDir = '%s/uploads' % BASE_DIR

MaxUploadFiles = 6  # max files number allowed by one single task

# WebSSH = ['localhost',4200] #deprecated

SHELLINABOX = {
    'host': '192.168.2.200',
    'port': 4200,
    'username': 'crazy_audit2',
    'password': '123'
}

SSH_CLIENT_PATH = '/usr/local/openssh7/bin/ssh'

SESSION_AUDIT_LOG_DIR = '%s/logs/audit' % BASE_DIR
SCHEDULE_LOG_DIR = '%s/logs/bernard/plan_logs' % BASE_DIR

LOG_LEVEL = logging.DEBUG

# for celery
CELERY_BROKER_URL = 'redis://localhost'
CELERY_RESULT_BACKEND = 'redis://localhost'
