from django.conf.urls import patterns, include, url
from django.contrib.gis import admin
from django.conf import settings # chargé pour ajouter la possibilité d'accéder au media_url/root lors d'appel dans les templates
from django.conf.urls.static import static # chargé pour ajouter la possibilité d'accéder au media_url/root lors d'appel dans les templates

urlpatterns = patterns('',
    url(r'^', include('home.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^map/', include('map.urls')),    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)