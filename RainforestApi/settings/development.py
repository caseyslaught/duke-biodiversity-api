from RainforestApi.settings.base import *


DEBUG = True
ALLOWED_HOSTS = ['*']

SECRET_KEY = 'django-insecure-7in5&#q8+kd)=l9_r=h%fzp+vq5kujd7h4r#a%@0kw@pfc2^h='

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

S3_DATA_PREFIX = 'development'
