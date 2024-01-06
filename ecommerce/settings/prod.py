from .common import *
import dj_database_url

DEBUG = False

SECRET_KEY =  os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['e-commerce-production-5fdc.up.railway.app']

DATABASES = {  
    'default': dj_database_url.config('MYSQL_URL')  
}

REDIS_URL = os.environ['REDIS_URL']

CELERY_BROKER_URL = REDIS_URL