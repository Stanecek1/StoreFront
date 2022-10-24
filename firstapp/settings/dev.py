from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v9s$qght4son$5!5pxk86k*_q21-=*i$)5*4j2!%+r9la&x#6)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront3',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': 'bayside1'
    }
}

# if DEBUG:
#     MIDDLEWARE += ['silk.middleware.SilkyMiddleware']