from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _
from atw.home import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(_(r'^project/$'), views.project, name='project'),
    url(_(r'^anaerobic-digestion/$'), views.ad, name='ad'),
    url(_(r'^waste-management/france/$'), views.wm_fr, name='wm_fr'),
    url(_(r'^sign-in/$'), views.sign_in, name='sign_in'),
    url(_(r'^sign-out/$'), views.sign_out, name='sign_out'),
    url(_(r'^register/$'), views.register, name='register'),
    url(_(r'^my-account/$'), views.my_account, name='my_account'),
)
