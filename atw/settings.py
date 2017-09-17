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
    'django.contrib.contenttypes',
    'grappelli.dashboard',
    'grappelli',  # before django.contrib.admin cette appli sert à l'appli filebrowser
    'filebrowser',  # before django.contrib.admin
    'modeltranslation',  # before django.contrib.admin
    'django.contrib.admin',  # Passer à django.contrib.admin.apps.SimpleAdminConfig quand on personnalise AdminSite et que part conséquent l'autodiscovery n'est plus nécessaire puisqu'on indiquera nous meme les modeles à intégrer
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django.contrib.sitemaps', reste à créer
    'django.contrib.gis',
    'django.contrib.syndication',  # pour le flux rss
    'haystack',
    'atw.home',
    'atw.map',
    'atw.article',
    'leaflet',
    'tinymce', # https://github.com/aljosa/django-tinymce
)

MIDDLEWARE_CLASSES = (  # A partir de Django 1.10 remplacer MIDDLEWARE_CLASSES par MIDDLEWARE
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.common.CommonMiddleware',  # nouveau dans Django 1.11
    'django.middleware.locale.LocaleMiddleware', # Added. https://docs.djangoproject.com/en/1.8/topics/i18n/translation/#how-django-discovers-language-preference'django.middleware.common.CommonMiddleware'
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'atw.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "atw", "admin", "templates")], # emplacement des templates qui permettent de modifier l'admin
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

LANGUAGE_CODE = 'fr' # default language Django will use if no translation is found. 'en-us' by default

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
    os.path.join(BASE_DIR, "atw", "article", "locale"),
)

# Leaflet
LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (45.75, 4.85), #(lat,lng)
    'DEFAULT_ZOOM': 3,
    'MIN_ZOOM': 2,
    'MAX_ZOOM': 18,
    'TILES': [('Watercolor', 'http://{s}.tile.stamen.com/watercolor/{z}/{x}/{y}.png', {'attribution': 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'}),
            ('Roads', 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {'attribution': 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a>'}),
            ('Outdoors', 'http://{s}.tile.thunderforest.com/outdoors/{z}/{x}/{y}.png', {'attribution': '&copy; <a href="http://www.opencyclemap.org">OpenCycleMap</a>, &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'}),
            ('Satellite', 'http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {'attribution': 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'}),
            ],
    'SCALE': None,
    'RESET_VIEW': False, # True by default : a button appears below the zoom controls and, when clicked, shows the entire map.

}

# Authentication
LOGIN_URL = '/sign-in/'
LOGOUT_URL = '/sign-out/'

#Thumbnails
#from easy_thumbnails.conf import Settings as thumbnail_settings

#THUMBNAIL_PRESERVE_EXTENSIONS = ('png',)
#THUMBNAIL_DEBUG = True

#THUMBNAIL_ALIASES = {
#    '': {
#        'small': {'size': (150, 80), 'crop': True},
#    },
#}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static") # directory where static files will be collected to. Never put anything in this directory myself.
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media") #directory that hold user-uploaded files
MEDIA_URL = '/media/' #URL that handles the media served from MEDIA_ROOT

media_uploads = os.path.join(MEDIA_ROOT, "uploads")
if not os.path.exists(media_uploads):
    os.makedirs(media_uploads)

# WYSIWYG Editor (TinyMCE 3.5)
TINYMCE_JS_URL = os.path.join(STATIC_URL, "tiny_mce/tiny_mce.js")
TINYMCE_JS_ROOT = os.path.join(STATIC_URL, "tiny_mce")
TINYMCE_DEFAULT_CONFIG = {
    # list of buttons : http://archive.tinymce.com/wiki.php/TinyMCE3x:Buttons/controls
    'plugins': "wordcount, emotions, print, table, media",
    #'spellchecker_language': "fr", # en by default
    'theme': "advanced",
    'width': '100%',
    'height': '600',
    'theme_advanced_buttons2_add': "separator, print",
    'theme_advanced_buttons3': "fontselect, fontsizeselect, forecolor, backcolor, sup, sub, separator, media, tablecontrols, separator, emotions, charmap",
    #'media_live_embeds': true, # Actif à parti de version 4.3
}
TINYMCE_FILEBROWSER = True
#TINYMCE_SPELLCHECKER = True

# Grappelli settings
GRAPPELLI_ADMIN_TITLE = 'WACS Admin'
GRAPPELLI_INDEX_DASHBOARD = 'atw.dashboard.CustomIndexDashboard'

# Filebrowser settings
FILEBROWSER_CONVERT_FILENAME = True
FILEBROWSER_DEFAULT_SORTING_BY = ('date','filename_lower')
FILEBROWSER_DEFAULT_SORTING_ORDER = 'asc'
FILEBROWSER_VERSIONS = {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Thumbnail (1 col)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'large': {'verbose_name': 'Large (8 col)', 'width': 680, 'height': '', 'opts': ''},
    '1024': {'verbose_name': 'Large (8 col)', 'width': 1024, 'height': '', 'opts': ''},
    '1024_576_cropped': {'verbose_name': '1024-576 TEL ', 'width': 1024, 'height': 576, 'opts': 'crop'},
    '1024_768_cropped': {'verbose_name': '1024-768 APN', 'width': 1024, 'height': 768, 'opts': 'crop'},
    '1024_cropped': {'verbose_name': '1024-1024', 'width': 1024, 'height': 1024, 'opts': 'crop'},
}
FILEBROWSER_ADMIN_VERSIONS = ['thumbnail', 'large', '1024', '1024_576_cropped', '1024_768_cropped', '1024_cropped']

# Haystack settings
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

if os.environ.get('DJANGO_ENV') == 'production':
    from settings_prod import *
else:
    from settings_dev import *
