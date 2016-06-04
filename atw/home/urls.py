from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _
from atw.home import views

urlpatterns = [
  url(_(r'^my-account/$'), views.my_account, name='my_account'),
  url(r'^$', views.home, name='home'),
  url(_(r'^short-hiking/$'), views.short_hinking, name='short_hiking'),
  url(_(r'^crossing-the-alps/$'), views.crossing_the_alps, name='crossing_the_alps'),
  url(_(r'^sign-in/$'), views.sign_in, name='sign_in'),
  url(_(r'^sign-out/$'), views.sign_out, name='sign_out'),
  url(_(r'^register/$'), views.register, name='register'),
  url(_(r'^my-account/$'), views.my_account, name='my_account'),
]
