from django.conf.urls import patterns, url
from home import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
	url(r'^project/$', views.project, name='project'),
	url(r'^anaerobic-digestion/$', views.ad, name='ad'),
	url(r'^waste-management/france/$', views.wm_fr, name='wm_fr'),
	url(r'^community/$', views.community, name='community'),
	url(r'^sign_in/$', views.sign_in, name='sign_in'),
	url(r'^sign_out/$', views.sign_out, name='sign_out'),
	url(r'^register/$', views.register, name='register'),
	url(r'^my_account/$', views.my_account, name='my_account'),
)