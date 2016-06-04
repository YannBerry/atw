from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _
from atw.article import views

urlpatterns = [
  url(_(r'^$'), views.article_menu, name='article_menu'),
  url(_(r'^geol$'), views.geol, name='geol'),
  url(_(r'^(?P<title>\w+)/$'), views.article, name='article'),
  url(_(r'^download-articles/pdf/$'), views.download_articles_pdf, name='download_articles_pdf'),
  url(_(r'^download-article/(?P<title>\w+)/pdf/$'), views.download_article_pdf, name='download_article_pdf'),
]