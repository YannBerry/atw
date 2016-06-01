# -*- coding: utf-8 -*-
"""
WSGI config for atw project hosted by biodigitals.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os
#import site
#import sys

#os.environ.setdefault("DJANGO_ENV", "production")
#if os.environ["DJANGO_ENV"] == 'production':
    ## Add the site-packages of the chosen virtualenv to work with
    #site.addsitedir('/srv/atw/local/lib/python2.7/site-packages')

    ## Add the app's directory to the PYTHONPATH
    #sys.path.append('/srv/atw/')

    ## Activate your virtual env
    #activate_env=os.path.expanduser("/srv/atw/bin/activate_this.py")
    #execfile(activate_env, dict(__file__=activate_env))
    
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "atw.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Whitenoise configuration
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)
