# Django settings for servermon project.
import os
from django.conf import global_settings
from django import VERSION as DJANGO_VERSION
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)


DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'CHANGE_THIS_IF_YOU_DONT_WANT_ALL_KINDS_OF_PROBLEMS'

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',             # Or path to database file if using sqlite3.
        'USER': '',             # Not used with sqlite3.
        'PASSWORD': '',         # Not used with sqlite3.
        'HOST': '',             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',             # Set to empty string for default. Not used with sqlite3.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# # calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Abuse STATIC_URL for now without having collectstatic and by having already
# provisioned an admin directory under static
STATIC_URL = '/static/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = here('staticfiles')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (here('static'), )

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'djangobackends.context_processors.installed_apps',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'djangobackends.StripWhitespaceMiddleware.StripWhitespaceMiddleware',
)

ROOT_URLCONF = 'servermon.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'servermon.wsgi.application'

TEMPLATE_DIRS = (
    here('templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# You probably want to uncomment pretty much everything here
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'projectwide',
    'updates',
    'puppet',
    'hwdoc',
    'keyvalue',
)

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
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


AUTHENTICATION_BACKENDS = (
    # 'djangobackends.ldapBackend.ldapBackend',
    'django.contrib.auth.backends.ModelBackend',
)

LDAP_AUTH_SETTINGS = (
    {'url': 'ldap://ldap.example.org/', 'base': 'ou=People,dc=example,dc=org'},
)

LDAP_AUTH_GROUP = 'not-auth'
LDAP_AUTH_IS_STAFF = True


# South
if DJANGO_VERSION[:2] < (1, 7):
    INSTALLED_APPS = INSTALLED_APPS + ('south',)

# Use the old pre 1.6 testrunner
if DJANGO_VERSION[:2] >= (1, 6):
    TEST_RUNNER = 'django.test.simple.DjangoTestSuiteRunner'

SKIP_SOUTH_TESTS = True

# Settings for puppet views
DATE_FORMAT = "d/m/Y H:i"
DATETIME_FORMAT = "d/m/Y H:i"
HOST_TIMEOUT = 1800
MANAGED_PUPPET_MODELS = False

# Ticketing
TICKETING_SYSTEM = 'dummy'  # dummy, comments, jira are possible values
COMMENTS_TICKETING_URL = 'http://ticketing.example.com/'
JIRA_TICKETING = {
    'url': 'http://ticketing.example.com/',
    'search_string': 'text ~ {}',  # {} replaced by double-quoted serial number for search
    'projects': {  # empty dict means "all projects"
        'project1': {'closed_string': 'closed'},
        'project2': {'closed_string': 'done'},
        'project3': {'closed_string': 'pining_for_the_fjords'},
        'project4': {},
    },
    'projects_defaults': {'closed_string': 'closed'},
    'auth': {
        'type': 'none',  # none, basic, oauth are possible values
        'user': '',                             # only used for basic
        'password': '',                         # only used for basic
        'access_token': '',                     # only used for oauth
        'access_token_secret': '',              # only used for oauth
        'consumer_key': 'jira-oauth-consumer',  # only used for oauth
        'key_cert': '/path/to/file',            # only used for oauth
    },
}

# Since Django 1.7 uses migrations for itself, move old South based migrations
# to their own directory
SOUTH_MIGRATION_MODULES = {
    'hwdoc': 'hwdoc.south_migrations',
    'updates': 'updates.south_migrations',
}

# Silence the erroneous 1_6.W001 check. It was removed in
# https://code.djangoproject.com/ticket/23469 anyway
SILENCED_SYSTEM_CHECKS = ['1_6.W001']

# Django extensions (apt-get install python-django-extensions)
try:
    import django_extensions  # noqa
    INSTALLED_APPS = INSTALLED_APPS + ('django_extensions',)
except ImportError:
    pass

if 'DATABASE_URL' in os.environ:
    SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG
    # Parse database configuration from $DATABASE_URL
    import dj_database_url
    DATABASES['default'] =  dj_database_url.config()
    # Do NOT Enable Connection Pooling (if desired). South does not play nice
    # DATABASES['default']['ENGINE'] = 'django_postgrespool'

    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # Allow all host headers
    ALLOWED_HOSTS = ['*']

    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    # STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
    MANAGED_PUPPET_MODELS = True

