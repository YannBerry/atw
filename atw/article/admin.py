from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title_fr', 'title_en', 'slug_fr', 'slug_en', 'description_fr', 'description_en']}),
    ]
    list_display = ('title', 'slug')
    list_editable = ['slug']
    prepopulated_fields = {"slug_fr": ("title_fr",), "slug_en": ("title_en",)}

admin.site.register(Article, ArticleAdmin)