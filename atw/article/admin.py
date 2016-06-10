from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'title_en', 'slug', 'slug_en', 'description', 'description_en']}),
    ]
    list_display = ('title', 'title_en', 'slug', 'slug_en')
    list_editable = ['title_en', 'slug', 'slug_en']
    prepopulated_fields = {"slug": ("title",), "slug_en": ("title_en",)}

admin.site.register(Article, ArticleAdmin)