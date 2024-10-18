from pathlib import Path

from journal_dobrynya.env_config import *

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = PROJECT_SECRET_KEY
DEBUG = PROJECT_DEBUG

ALLOWED_HOSTS = [PROJECT_DOMAIN_NAME]

# FOR LOCUST
# ALLOWED_HOSTS = ["localhost"]
# CSRF_COOKIE_SECURE = False
# CSRF_COOKIE_HTTPONLY = True
# CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:8000']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'colorfield',
    'rest_framework',

    'mainapp.apps.MainappConfig',
    'users.apps.UsersConfig',
    'news.apps.NewsConfig',
    'tasks.apps.TasksConfig',
    'app_schedules.apps.AppSchedulesConfig',
    'attendance.apps.AttendanceConfig',
    'stats.apps.StatsConfig',
    'telebot.apps.TelebotConfig',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'journal_dobrynya.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'tasks.context_processors.quantity_new_task_user',
                'tasks.context_processors.quantity_check_task_user',
            ],
        },
    },
]

WSGI_APPLICATION = 'journal_dobrynya.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
        'OPTIONS': {'charset': DB_OPTIONS},
        'ATOMIC_REQUESTS': DB_ATOMIC_REQUESTS,
    },
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


LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Europe/Samara'

USE_I18N = True
USE_TZ = False

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = PROJECT_EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = PROJECT_EMAIL_HOST_PASSWORD

DOMAIN_NAME = PROJECT_DOMAIN_NAME
LOGIN_URL = 'login'

SECURE_SSL_REDIRECT = CONFIG__SECURE_SSL_REDIRECT
SECURE_HSTS_SECONDS = CONFIG__SECURE_HSTS_SECONDS
SESSION_COOKIE_SECURE = CONFIG__SESSION_COOKIE_SECURE
CSRF_COOKIE_SECURE = CONFIG__CSRF_COOKIE_SECURE
SECURE_HSTS_INCLUDE_SUBDOMAINS = CONFIG__SECURE_HSTS_INCLUDE_SUBDOMAINS
SECURE_HSTS_PRELOAD = CONFIG__SECURE_HSTS_PRELOAD
