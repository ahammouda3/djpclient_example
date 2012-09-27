# Django settings for djpclient_example project.

import os
import dj_database_url

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

SETTINGS_PATH = os.path.dirname(__file__)

if os.environ['CURRENT_ENVIRONMENT'] == 'PROD':
    CURRENT_ENVIRONMENT = 'PROD'
else:
    CURRENT_ENVIRONMENT = 'DEV'

# --------------------------------------------------
# PROFILER SETTINGS
# --------------------------------------------------
# note: when turning celery transmission on
# make sure to have celery running by running:
# python manage.py celeryd -E --loglevel=info
DJP_SEND_IN_CELERY_QUEUE = False

# note: celery will display some warnings if you have DEBUG = True; you can ignore these

# if not using celery, data will be transmitted in a separate thread
# if you desire you can delay the data transmission to ensure your web server has completely
# returned the request before submitting a POST; this is helpful if you have middleware
# or any piece of code that modifies the response in an expensive way once the template is rendered
DJP_SEND_DELAY = 1.0


# credentials for djangoperformance.com demo account.
# demo account username / password = demo / demo
if CURRENT_ENVIRONMENT == 'DEV':
    DJP_APP_NAME = 'djpclient_example'
    DJP_APP_USERNAME = 'ahammouda@uchicago.edu'
    DJP_API_KEY = '52a23dce5012c1522eddf2483920926c622d87d3' #For sending to staging djpsite
    #DJP_API_KEY = 'e46c83b5992082a97b28df8532f67b74cefd5eab' # For sending to dev-djpsite
else:
    DJP_APP_NAME = 'exampleapp'
    DJP_APP_USERNAME = 'ahammouda@uchicago.edu'
    DJP_API_KEY = 'e46c83b5992082a97b28df8532f67b74cefd5eab'
    
USE_BUNDLED_ENDPOINT = True
PROFILE_QUERIES = False
PROFILE_BENCHMARKS = False
PROFILE_MEMCACHE_STATS = False #Won't work without caching set up
PROFILE_USER_ACTIVITY = False

#---------------------------------
# Analytics settings for djpclient
#---------------------------------
TRACK_GOOGLE_ANALYTICS = True
GA_PROFILE_ID = 'UA-33670488-2'
if CURRENT_ENVIRONMENT == 'PROD':
    SESSION_COOKIE_DOMAIN = 'http://www.http://djpclient-example.herokuapp.com'
else:
    SESSION_COOKIE_DOMAIN = 'http://localhost:7000'


#for debugging
#DJP_API_KEY = '493b0c8936a282ca1ea1eee47a61d1b80ee7090d'

if CURRENT_ENVIRONMENT == 'DEV':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'data.db',                      # Or path to database file if using sqlite3.
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
            }
        }
else:
    DATABASE_URL = os.environ['HEROKU_POSTGRESQL_BLUE_URL']
    DATABASES = {'default': dj_database_url.parse(DATABASE_URL)}


# --------------------------------------------------
# CACHE SETTINGS
# --------------------------------------------------
#CACHE_BACKEND = 'file://%s/file_cache' % (SETTINGS_PATH,)

# uncomment this line to use python-memcached for the cache backend
#CACHE_BACKEND = 'memcached://127.0.0.1:11211/'


#SESSION_SAVE_EVERY_REQUEST = True
#SESSION_COOKIE_NAME='ga-report-id'
SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_FILE_PATH = '/%s/session_file' % (SETTINGS_PATH,)

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 't3si#w-q&amp;m8^&amp;l^lv!1=u+ogd#qv672*ps3l4^vre$8u9s51sl'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
#    'django.template.loaders',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'djpclient_example.djpclient.djpclient.middleware.DJPClientMiddleware',
    
    
    # uncomment this line to profile the entie client application (recommended)
    
    
    # middleware for site-wide caching
#    'django.middleware.cache.UpdateCacheMiddleware',
#    'django.middleware.common.CommonMiddleware',
#    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'djpclient_example.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'djpclient_example.wsgi.application'

TEMPLATE_PATH = os.path.join(SETTINGS_PATH, 'templates')

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    TEMPLATE_PATH,
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'djpclient_example.books',
    
    'djpclient_example.djpclient.djpclient',
    
    #'kombu.transport.django',
    #'djcelery',
)


# -----------------------------------------------------------
# CELERY CONFIGURATION
# -----------------------------------------------------------
BROKER_BACKEND = 'django'
BROKER_HOST = DATABASES['default']['HOST']
BROKER_USER = DATABASES['default']['USER']
BROKER_PASSWORD = DATABASES['default']['PASSWORD']

#import djcelery
#djcelery.setup_loader()



# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
'''
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'djp_handler': {
            'level': 'INFO',
            'class': 'djpclient.log.DJPHandler',
        }
    },
    'loggers': {
        'djpclient_example.books.views': {
            'handlers': ['djp_handler'],
            'level': 'INFO',
            'propagate': True
        },
        'djplogger': {
            'handlers': ['djp_handler'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}
'''
