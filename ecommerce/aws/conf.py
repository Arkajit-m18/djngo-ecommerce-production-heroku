import datetime, os

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', "AKIAWSI5VAVSCDTOF6PT")
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', "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")
AWS_USERNAME = "arkajit-ecommerce-django"
AWS_GROUPNAME = "django-ecommerce-group"
AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False
AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = 'ecommerce.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'ecommerce.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'django-ecommerce-aws-bucket'
S3DIRECT_REGION = 'us-east-1'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = { 
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}