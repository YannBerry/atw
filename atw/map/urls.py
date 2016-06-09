from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _
from atw.map import views
from atw.map.feeds import LatestStageFeed


urlpatterns = [
    url(r'^$', views.osmap, name='map'),
    url(_(r'^gmap/$'), views.gmap, name='gmap'),
    url(_(r'^trip/(?P<id>[0-9]+)/$'), views.trip, name='trip'),
    url(_(r'^trip-stage/(?P<id>[0-9]+)/$'), views.trip_stage, name='trip_stage'),
    url(_(r'^add-trip-stage/$'), views.add_trip_stage, name='add_trip_stage'),
    url(_(r'^add-trip-stage/success/$'), views.form_success, name='trip_stage_added'),
    url(_(r'^list-trips/$'), views.list_trips, name='list_trips'),
    url(_(r'^list-trips/download-pdf/$'), views.list_trips_pdf, name='list_trips_pdf'),
    url(_(r'^list-trips/download-csv/$'), views.list_trips_csv, name='list_trips_csv'),
    url(_(r'^list-trips/trip-stages/download-pdf/$'), views.list_trip_stages_pdf, name='list_trip_stages_pdf'),
    url(_(r'^list-trips/trip-stages/download-csv/$'), views.list_trip_stages_csv, name='list_trip_stages_csv'),
    url(_(r'^latest-stages/feed/$'), LatestStageFeed(), name='trip_stage_feed'),
]
