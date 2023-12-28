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
        'HOST': '127.0.0.1',  
        'PORT': '3306',  
        'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        }  
    }  
}  