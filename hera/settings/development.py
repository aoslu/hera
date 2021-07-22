from .base import *

DEBUG=True

ALLOWED_HOSTS=['*']

AWS_ACCESS_KEY_ID = env('ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'herakomurculukbucket'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS= {
    'CacheControl':'max-age=86400',
}
AWS_LOCATION = 'static'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


DEFAULT_FILE_STORAGE= 'hera.storage_backend.MediaStorage'