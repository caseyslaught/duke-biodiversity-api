import os

from RainforestApi.settings.base import *


DEBUG = True
ALLOWED_HOSTS = ['rainforest-production.eba-tgpybk9s.us-east-1.elasticbeanstalk.com']

SECRET_KEY = os.environ['DUKE_RAINFOREST_SECRET']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rainforest_production',
        'USER': 'admin',
        'PASSWORD': os.environ['DUKE_RAINFOREST_MYSQL_PASSWORD'],
        'HOST': os.environ['DUKE_RAINFOREST_MYSQL_HOST'],
        'PORT': '3306',
    },
    'OPTIONS': {
        'charset': 'utf8mb4',
        'use_unicode': True,
    }
}

S3_DATA_PREFIX = 'production'

