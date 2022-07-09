from .base import *

DEBUG = True

ALLOWED_HOSTS = ['proyectomoises.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd8a6i3oarqp0ki',
        'USER': 'zmtrjsodzyeijv',
        'PASSWORD': '2b998cd5b434683e9d981d43087c18eb80ca197adfc120deb1732d07d59b5088',
        'HOST': 'ec2-34-233-115-14.compute-1.amazonaws.com',
        'PORT': 5432
    }
}