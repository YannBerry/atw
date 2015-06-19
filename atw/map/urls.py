from django.conf.urls import patterns, url
from map import views

urlpatterns = patterns('',
	url(r'^$', views.map, name='map'),
	url(r'^gmap/$', views.gmap, name='gmap'),
    url(r'^add-point/$', views.add_point, name='add_point'),
    url(r'^add-point/success/$', views.form_success, name='point_added'),
    url(r'^add-point/error/$', views.form_error, name='point_error'),
    url(r'^download-db/$', views.download_db, name='download_db'),    
	url(r'^download-db/pdf/$', views.download_db_pdf, name='download_db_pdf'),
	url(r'^download-db/csv/$', views.download_db_csv, name='download_db_csv'),
)