from django.db import models
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField

class Article(models.Model):
    title = models.CharField(verbose_name=_("Article"), max_length=25)
    description = HTMLField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")