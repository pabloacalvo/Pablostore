from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        "OPTIONS":{
            "read_default_file":"settings/my.cnf"
        }

    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True