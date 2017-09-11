from django.db import models
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField


class Article(models.Model):
    title = models.CharField(verbose_name=_("Titre"), max_length=25)
    slug = models.SlugField(_("Slug"), max_length=50, unique=True)
    description = HTMLField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")