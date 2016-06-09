#-*- coding: utf-8 -*-

import datetime # Python’s standard datetime module
from django.contrib.gis.db import models
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone # https://docs.djangoproject.com/en/1.7/topics/i18n/timezones/ + answers to basic questions : https://docs.djangoproject.com/en/1.7/topics/i18n/timezones/#time-zones-faq
from django.core.validators import MinValueValidator
from tinymce.models import HTMLField
from filebrowser.fields import FileBrowseField

class Massif(models.Model):
    massif = models.CharField(verbose_name=_("Massif"), max_length=25)

    def __str__(self):
        return self.massif

    class Meta:
        ordering = ['massif']
        verbose_name = _("Massif")
        verbose_name_plural = _("Massifs")

class Type(models.Model):
    type = models.CharField(verbose_name=_("Type"), max_length=25)

    def __str__(self):
        return self.type

    class Meta:
        ordering = ['type']
        verbose_name = _("Type")
        verbose_name_plural = _("Types")

class Trip(models.Model):
    trip_name = models.CharField(verbose_name=_("Trip Name"), max_length=50)
    trip_slug = models.SlugField(_("Slug"), max_length=50, unique=True)
    prepopulated_fields = {"trip_slug": ("trip_name",)} # does not work
    start_date = models.DateField(verbose_name=_("Start date"), default=timezone.now, blank=True)
    end_date = models.DateField(verbose_name=_("End date"), default=timezone.now, blank=True)
    nbr_of_days = models.IntegerField(verbose_name=_("Nbr of days"), blank=True)
    date_published = models.DateTimeField(verbose_name=_("Date published"), auto_now_add=True)
    description = HTMLField(blank=True)
    geom = models.PointField(srid=4326, default='POINT(5.0 44.5)')
    #picture_tag = models.ImageField(verbose_name=_("Picture tag"), upload_to='picture/%Y/%m', blank=True, null=True)
    picture_tag = FileBrowseField(verbose_name=_("Picture tag"), max_length=200, directory="uploads/picture/%Y/%m", extensions=[".jpg"], blank=True, null=True)

    objects = models.GeoManager()

    class Meta:
        ordering = ["start_date"]
        verbose_name = _("Trip")
        verbose_name_plural = _("Trips")

    def __str__(self):
        return '{0} ({1})'.format(self.trip_name, self.start_date)

    def save(self, *args, **kwargs):
        if self.start_date and self.end_date:
            self.nbr_of_days = self.end_date.day - self.start_date.day + 1
        super().save(*args, **kwargs)

    def display_picture_tag(self): # Display the picture in the admin interface instead of just displaying a link to the picture
        if self.picture_tag:
            return '<img style="max-width:100%;" src="{}" />'.format(self.picture_tag.url)
    display_picture_tag.allow_tags = True

class TripStage(models.Model):
    stage_name = models.CharField(verbose_name=_("Stage Name"), max_length=50)
    stage_slug = models.SlugField(_("Slug"), max_length=50, unique=True)
    prepopulated_fields = {"stage_slug": ("stage_name",)} # does not work
    date = models.DateField(verbose_name=_("Date"), default=timezone.now, blank=True)
    date_published = models.DateTimeField(verbose_name=_("Date published"), auto_now_add=True)
    massif = models.ForeignKey(Massif, verbose_name = _("Massif"), null=True, blank=True) # Voir comment on fait des cleaned data avec des foreign keys dans un formulaire avec Django car lui il compare le text à l'id du status défini dans modèle status
    type = models.ForeignKey(Type, verbose_name = _("Type"))
    #picture_tag = models.ImageField(verbose_name=_("Picture tag"), upload_to='uploads/picture/%Y/%m', blank=True, null=True)
    picture_tag = FileBrowseField(verbose_name=_("Picture tag"), max_length=200, directory="uploads/picture/%Y/%m", extensions=[".jpg"], blank=True, null=True)
    story = HTMLField(blank=True)
    duration = models.IntegerField(verbose_name=_("Duration (h)"), blank=True, null=True, validators=[MinValueValidator(0)])
    distance = models.IntegerField(verbose_name=_("Distance (km)"), blank=True, null=True, validators=[MinValueValidator(0)])
    geom = models.PointField(srid=4326, default='POINT(5.0 44.5)') #srid=4326 doit être la valeur par défaut je pense mais je l'écris quand même
    email_validation = models.BooleanField(verbose_name=_("Email validation"))
    email = models.EmailField(verbose_name=_("E-mail adress"), blank=True, null=True)
    added_by = models.CharField(verbose_name=_("Added by"), max_length=50, default="Admin")
    trips = models.ManyToManyField(Trip, verbose_name=_("Trips"))

    objects = models.GeoManager() # Allows to perform geoqueryset https://docs.djangoproject.com/en/1.7/ref/contrib/gis/model-api/#geomanager. Geoqueryset class : https://docs.djangoproject.com/en/1.7/ref/contrib/gis/geoquerysets/#django.contrib.gis.db.models.GeoQuerySet

    def __str__(self):
        return '{0} ({1})'.format(self.stage_name, self.date)

    def published_more_than_6_months_ago(self):
        return self.date_published <= timezone.now() - datetime.timedelta(days=180) # http://sametmax.com/manipuler-les-dates-et-les-durees-en-python/

    def display_picture_tag(self): # Display the picture in the admin interface instead of just displaying a link to the picture
        if self.picture_tag:
            return '<img style="max-width:100%;" src="{}" />'.format(self.picture_tag.url)
    display_picture_tag.allow_tags = True

    class Meta:
        ordering = ["date"]
        verbose_name = _("Stage")
        verbose_name_plural = _("Stages")

#class TripStageTrip(models.Model):
    #trip = models.ForeignKey(Trip)
    #tripstage = models.ForeignKey(TripStage)

