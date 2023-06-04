from .base import *
import os
SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['136.243.9.185','csestudent.com','www.csestudent.com']

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': os.environ.get('DB_NAME'),
        'HOST':'localhost',
        'PORT': '3306',
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'SQL_MODE': 'NO_AUTO_VALUE_ON_ZERO',
        'OPTIONS': {
            'autocommit': True,
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES', innodb_strict_mode=1",
            'charset': 'utf8mb4',
        },
        'TEST': {
            'CHARSET': 'utf8mb4',
            'COLLATION': 'utf8mb4_unicode_ci',
        }
    
    }
}

STATIC_ROOT = '/home/csestude/public_html/my_blog/static/'
MEDIA_ROOT = '/home/csestude/public_html/my_blog/media/'