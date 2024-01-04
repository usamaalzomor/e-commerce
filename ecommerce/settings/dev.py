from .common import *


DEBUG = True

SECRET_KEY = 'django-insecure-up%vg+92^kx1mq^gmz2jyx7gs%3!kj6^$@=2%i5ufy^r6r8ghh'

if DEBUG:
    MIDDLEWARE += ['silk.middleware.SilkyMiddleware']

DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'ecommerce3',  
        'USER': 'root',  
        'PASSWORD': 'Osa_05910120',  
        'HOST': 'mysql',  
        'PORT': '3306',  
        'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        }  
    }  
}

CELERY_BROKER_URL = 'redis://redis:6379/1'

EMAIL_HOST ='smtp4dev'
EMAIL_HOST_USER =''
EMAIL_HOST_PASSWORD =''
EMAIL_PORT = 2525

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True
}