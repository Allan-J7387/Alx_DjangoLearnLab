from pathlib import Path


ROOT_URLCONF = 'social_media_api.urls'
WSGI_APPLICATION = 'social_media_api.wsgi.application'


DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': BASE_DIR / 'db.sqlite3',
}
}


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True
USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# DRF basics
REST_FRAMEWORK = {
'DEFAULT_AUTHENTICATION_CLASSES': [
'rest_framework.authentication.SessionAuthentication',
'rest_framework.authentication.BasicAuthentication',
],
'DEFAULT_PERMISSION_CLASSES': [
'rest_framework.permissions.AllowAny',
],
}


CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS', '').split(',') if os.getenv('CSRF_TRUSTED_ORIGINS') else []
CORS_ALLOWED_ORIGINS = os.getenv('CORS_ALLOWED_ORIGINS', '').split(',') if os.getenv('CORS_ALLOWED_ORIGINS') else []


# Logging (overridden/expanded in production)
LOGGING = {
'version': 1,
'disable_existing_loggers': False,
'handlers': {
'console': {
'class': 'logging.StreamHandler',
},
},
'root': {
'handlers': ['console'],
'level': 'INFO',
},
}