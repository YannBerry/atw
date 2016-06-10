from modeltranslation.translator import translator, TranslationOptions
from atw.article.models import Article

class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', 'description',)

translator.register(Article, ArticleTranslationOptions)