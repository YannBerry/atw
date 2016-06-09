# encoding: utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

from atw.article.models import Article
#from tinymce.models import HTMLField
from haystack import indexes


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    #title = indexes.CharField(model_attr='title')
    #description = indexes.HTMLField(model_attr='description')

    def get_model(self):
        return Article

    #def index_queryset(self, using=None):
        #return self.get_model().objects.filter(public=True)
