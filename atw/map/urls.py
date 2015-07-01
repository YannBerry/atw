from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _
from atw.map import views

urlpatterns = patterns('',
    url(r'^$', views.map, name='map'),
    url(_(r'^gmap/$'), views.gmap, name='gmap'),
    url(_(r'^add-point/$'), views.add_point, name='add_point'),
    url(_(r'^add-point/success/$'), views.form_success, name='point_added'),
    url(_(r'^download-db/$'), views.download_db, name='download_db'),
    url(_(r'^download-db/pdf/$'), views.download_db_pdf, name='download_db_pdf'),
    url(_(r'^download-db/csv/$'), views.download_db_csv, name='download_db_csv'),
)
