#-*- coding: utf-8 -*-

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECRET_KEY in settings_dev.py

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get('DJANGO_ENV') == 'production':
    DEBUG = False
else:
    DEBUG = True


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin', # Passer à django.contrib.admin.apps.SimpleAdminConfig quand on personnalise AdminSite et que part conséquent l'autodiscovery n'est plus nécessaire puisqu'on indiquera nous meme les modeles à intégrer
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django.contrib.sitemaps', reste à créer
    'django.contrib.gis',
    'easy_thumbnails',
    'widget_tweaks', # https://github.com/kmike/django-widget-tweaks Permet d'ajouter des filtres aux templates des forms (ajout css, attributs, etc.)
    'atw.home',
    'atw.map',
    'leaflet',
    'debug_toolbar',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', # Added. https://docs.djangoproject.com/en/1.8/topics/i18n/translation/#how-django-discovers-language-preference'django.middleware.common.CommonMiddleware'
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'atw.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "atw", "admin", "templates")],
        'APP_DIRS': True, # obligatoire pour utiliser l'application sitemap
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n', # Added https://docs.djangoproject.com/en/1.8/topics/i18n/translation/#get-current-language-bidi
                #'django.template.context_processors.csrf' pas nécessaire de l'ajouter car il est ajouté de force.
            ],
        },
    },
]



# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

#DATABASES in settings_dev.py

#Email in settings_dev.py


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us' # default language Django will use if no translation is found

TIME_ZONE = 'Europe/Paris' # https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-TIME_ZONE

USE_I18N = True

USE_L10N = True # controls whether Django should activate format localization (date, number, etc.) https://docs.djangoproject.com/en/1.7/ref/settings/#std:setting-USE_L10N

USE_TZ = True # https://docs.djangoproject.com/fr/1.8/topics/i18n/timezones/#naive-and-aware-datetime-objects

LANGUAGES = (
    ('fr', _('French')),
    ('en', _('English')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "atw", "home", "locale"),
    os.path.join(BASE_DIR, "atw", "map", "locale"),
)

# Leaflet
LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (45.75, 4.85), #(lat,lng)
    'DEFAULT_ZOOM': 3,
    'MIN_ZOOM': 2,
    'MAX_ZOOM': 18,
    'TILES': [('Watercolor', 'http://{s}.tile.stamen.com/watercolor/{z}/{x}/{y}.png', {'attribution': 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'}),
            ('Roads', 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {'attribution': 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a>'}),
            ('Satellite', 'http://{s}.tile.thunderforest.com/outdoors/{z}/{x}/{y}.png', {'attribution': '&copy; <a href="http://www.opencyclemap.org">OpenCycleMap</a>, &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'}),
            ('Satellite2', 'http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {'attribution': 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'}),
            ('Hybrid', 'http://{s}.{base}.maps.cit.api.here.com/maptile/2.1/maptile/{mapID}/hybrid.day/{z}/{x}/{y}/256/png8?app_id={app_id}&app_code={app_code}', {'attribution': 'Map &copy; 1987-2014 <a href="http://developer.here.com">HERE</a>', 'subdomains': '1234', 'mapID': 'newest', 'app_id': 'Y8m9dK2brESDPGJPdrvs', 'app_code': 'dq2MYIvjAotR8tHvY8Q_Dg', 'base': 'aerial', 'minZoom': 0, 'maxZoom': 20}),
            ],
    'SCALE': None,
    'RESET_VIEW': False, # True by default : a button appears below the zoom controls and, when clicked, shows the entire map.

}

# Authentication
LOGIN_URL = '/sign-in/'
LOGOUT_URL = '/sign-out/'

#Thumbnails
from easy_thumbnails.conf import Settings as thumbnail_settings

THUMBNAIL_PRESERVE_EXTENSIONS = ('png',)
THUMBNAIL_DEBUG = True

THUMBNAIL_ALIASES = {
    '': {
        'small': {'size': (150, 80), 'crop': True},
    },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static") # directory where static files will be collected to. Never put anything in this directory myself.
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media") #directory that hold user-uploaded files
MEDIA_URL = '/media/' #URL that handles the media served from MEDIA_ROOT

if os.environ.get('DJANGO_ENV') == 'production':
    from settings_prod import *
else:
    from settings_dev import *

