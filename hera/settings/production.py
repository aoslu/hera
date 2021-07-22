from .base import *
import environ


DEBUG=False
ALLOWED_HOSTS = ['*']

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [

]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DEV ORTAMINA ÖZEL DB.

DATABASES={
   'default':{
      'ENGINE':'django.db.backends.postgresql_psycopg2',
      'NAME': env('DB_NAME'),
      'USER': env('DB_USER'),
      'PASSWORD': env('DB_PASSWORD'),
      'HOST': 'localhost',
      'PORT': '5432',
   }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]