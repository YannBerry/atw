import datetime # Python’s standard datetime module
from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone # https://docs.djangoproject.com/en/1.7/topics/i18n/timezones/ + answers to basic questions : https://docs.djangoproject.com/en/1.7/topics/i18n/timezones/#time-zones-faq
from django.core.validators import MinValueValidator

class Status(models.Model):
    status = models.CharField(verbose_name=_("Status"), max_length=25)

    def __str__(self):
        return self.status

    class Meta:
        ordering = ['status']
        verbose_name_plural = _("Status")

class Stage(models.Model):
    stage = models.CharField(verbose_name=_("Stage"), max_length=25)

    def __str__(self):
        return self.stage

    class Meta:
        ordering = ['stage']

class Initiative(models.Model):
    project_name = models.CharField(verbose_name=_("Project Name"), max_length=50)
    status = models.ForeignKey(Status) # Voir comment on fait des cleaned data avec des foreign keys dans un formulaire avec Django car lui il compare le text à l'id du status défini dans modèle status
    stage = models.ForeignKey(Stage)
    project_leader = models.CharField(verbose_name=_("Project Leader"), max_length=50)
    picture = models.ImageField(verbose_name=_("Picture"), upload_to='picture/%Y/%m', blank=True, null=True)
    description = models.TextField(blank=True)
    nbr_installations = models.IntegerField(verbose_name=_("Number of Installations"), blank=True, null=True, validators=[MinValueValidator(0)])
    power = models.IntegerField(verbose_name=_("Total Power (kW)"), blank=True, null=True, validators=[MinValueValidator(0)])
    start = models.DateField(verbose_name=_("Beginning of the project"), default=timezone.now, blank=True)
    date_published = models.DateTimeField(verbose_name=_("Date published"), auto_now_add=True)
    geom = models.PointField(srid=4326) #srid=4326 doit être la valeur par défaut je pense mais je l'écris quand même
    email_validation = models.BooleanField(verbose_name=_("Email validation"))
    email = models.EmailField(verbose_name=_("E-mail adress"), blank=True, null=True)
    added_by = models.CharField(verbose_name=_("Added by"), max_length=50)

    objects = models.GeoManager() # Allows to perform geoqueryset https://docs.djangoproject.com/en/1.7/ref/contrib/gis/model-api/#geomanager. Geoqueryset class : https://docs.djangoproject.com/en/1.7/ref/contrib/gis/geoquerysets/#django.contrib.gis.db.models.GeoQuerySet

    def __str__(self):
        return '{0} ({1})'.format(self.project_name, self.project_leader)

    def published_more_than_6_months_ago(self):
        return self.date_published <= timezone.now() - datetime.timedelta(days=180) # http://sametmax.com/manipuler-les-dates-et-les-durees-en-python/

    def picture_tag(self): # Display the picture in the admin interface instead of just displaying a link to the picture
        if self.picture:
            return '<img style="max-width:100%;" src="{}" />'.format(self.picture.url)
    picture_tag.allow_tags = True

    class Meta:
        verbose_name = _("AD Initiative")
        verbose_name_plural = _("AD Initiatives")
