#-*- coding: utf-8 -*-

"""atw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import patterns, include, url
from django.contrib.gis import admin
from django.conf import settings # chargé pour ajouter la possibilité d'accéder au media_url/root lors d'appel dans les templates
from django.conf.urls.static import static # chargé pour ajouter la possibilité d'accéder au media_url/root lors d'appel dans les templates
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _

urlpatterns = patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')), # default name : set_language, ne doit pas être mis dans i18n
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    url(r'^', include('atw.home.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(_(r'^map/'), include('atw.map.urls')),
)
