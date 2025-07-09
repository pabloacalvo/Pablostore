from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        "OPTIONS":{
            "read_default_file":"otraruta/my.cnf"
        }

    }
}