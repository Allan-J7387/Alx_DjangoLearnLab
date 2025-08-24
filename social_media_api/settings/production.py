from .base import * # noqa
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'


# HSTS (enable once HTTPS works)
SECURE_HSTS_SECONDS = int(os.getenv('SECURE_HSTS_SECONDS', '31536000'))
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True


# Database from DATABASE_URL (e.g., Postgres)
# Example: postgres://USER:PASSWORD@HOST:PORT/NAME
import dj_database_url
DATABASES = {
'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}


# Static/Media – Option A: WhiteNoise for static, local media (small projects)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Static/Media – Option B: S3 for both (uncomment when ready)
# INSTALLED_APPS += ['storages']
# AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
# AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME', 'us-east-1')
# AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STORAGES = {
# "default": {
# "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
# },
# "staticfiles": {
# "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
# },
# }
# STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
# MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"


# Email (for error alerts)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST', '')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', '587'))
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'no-reply@your-domain.com')


# Better logging for production
LOGGING['handlers']['file'] = {
'class': 'logging.FileHandler',
'filename': os.getenv('DJANGO_LOG_FILE', '/var/log/django/app.log'),
}
LOGGING['root'] = {
'handlers': ['console', 'file'],
'level': 'INFO',
}

DEBUG = os.getenv("DEBUG", "False").lower() == "true"

