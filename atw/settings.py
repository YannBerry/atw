"""
Django settings for Site project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u4%!bg5$0^iv8-q)dspoj!4py4s(yvdp!r*@^pn6%8pag%80@2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin', # Passer à django.contrib.admin.apps.SimpleAdminConfig quand on personnalise AdminSite et que part conséquent l'autodiscovery n'est plus nécessaire puisqu'on indiquera nous meme les modeles à intégrer
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'home',
    'map',
    'leaflet',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Site.urls'

WSGI_APPLICATION = 'Site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'db', 
        'USER': 'postgres',
        'PASSWORD': 'saew5oex',
        'HOST': '127.0.0.1',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',      # Set to empty string for default.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True # controls whether Django should activate format localization (date, number, etc.) https://docs.djangoproject.com/en/1.7/ref/settings/#std:setting-USE_L10N

USE_TZ = True


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
LOGIN_URL = '/sign_in/'
LOGOUT_URL = '/sign_out/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

if DEBUG:
    MEDIA_ROOT = os.path.join(BASE_DIR, "static", "media") #directory that hold user-uploaded files
    MEDIA_URL = '/media/' #URL that handles the media served from MEDIA_ROOT
    STATIC_ROOT = os.path.join(BASE_DIR, "static", "static") # directory where static files will be collected to. Never put anything in this directory myself.