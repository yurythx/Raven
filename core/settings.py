"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
import sys
from pathlib import Path

from corsheaders.defaults import default_headers 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Diz para Django onde estão nossos aplicativos
APPS_DIR = str(os.path.join(BASE_DIR,'apps'))
sys.path.insert(0, APPS_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5iy^d-bu8b2yaat7j))09j8@6=8=ay%qwul^yn3qnvm2jqpkpi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.humanize',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    "corsheaders",
    "crispy_forms",
    "crispy_bootstrap5",
    
   
   
    "django_summernote",
 

    #'apps.config',
    
    'apps.blog', 
    'apps.pages', 
    
    
    
    
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware', #time out
    "corsheaders.middleware.CorsMiddleware", #cors
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'requestlogs.middleware.RequestLogsMiddleware', #logs
     
]

CORS_ALLOW_HEADERS = list(default_headers) + [
                                'X-Register',
                        ]

                        # CORS Config
CORS_ORIGIN_ALLOW_ALL = True  
                        # CORS_ORIGIN_ALLOW_ALL como True, o que permite que qualquer site acesse seus recursos.
                        # Defina como False e adicione o site no CORS_ORIGIN_WHITELIST onde somente o site da lista acesse os seus recursos.

CORS_ALLOW_CREDENTIALS = False 

CORS_ORIGIN_WHITELIST = ['http://meusite.com',] # Lista. 


ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        #'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

REST_FRAMEWORK={
            
            'EXCEPTION_HANDLER': 'requestlogs.views.exception_handler',
        }
       # Documentação: https://docs.djangoproject.com/en/4.1/topics/logging/#topic-logging-parts-loggers

        # Logs
LOGGING = {
            'version': 1,
            'disable_existing_loggers': False,
            'handlers': {
                'requestlogs_to_file': {
                    'level': 'INFO',
                    'class': 'logging.FileHandler',
                    'filename': 'info.log',
                },
            },
            'loggers': {
                'requestlogs': {
                    'handlers': ['requestlogs_to_file'],
                    'level': 'INFO',
                    'propagate': False,
                },
            },
        }

REQUESTLOGS = {
            'SECRETS': ['password', 'token'],
            'METHODS': ('PUT', 'PATCH', 'POST', 'DELETE'),
        }

 # timeout tempo de inatividate no sistema
SESSION_EXPIRE_SECONDS = 1800 
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
#SESSION_EXPIRE_AFTER_LAST_ACTIVITY_GRACE_PERIOD = 60  
SESSION_TIMEOUT_REDIRECT = 'http://localhost:8000/'

SESSION_TIMEOUT_REDIRECT = 'http://localhost:8000/pages/desconectado-inatividade/'


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- Messages --- #

from django.contrib.messages import constants

MESSAGE_TAGS = {
	constants.ERROR: 'alert-danger',
	constants.WARNING: 'alert-warning',
	constants.DEBUG: 'alert-danger',
	constants.SUCCESS: 'alert-success',
	constants.INFO: 'alert-info',
}

X_FRAME_OPTIONS = 'SAMEORIGIN'

SUMMERNOTE_THEME = 'bs4'


