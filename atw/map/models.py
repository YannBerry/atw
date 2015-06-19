#import datetime
from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy
#from django.utils import timezone # https://docs.djangoproject.com/en/1.7/topics/i18n/timezones/ + answers to basic questions : https://docs.djangoproject.com/en/1.7/topics/i18n/timezones/#time-zones-faq

class Status(models.Model):
	status = models.CharField(max_length=25)

	def __str__(self):
		return self.status

class Stage(models.Model):
	stage = models.CharField(max_length=25)

	def __str__(self):
		return self.stage

class Initiative(models.Model):
	project_name = models.CharField(verbose_name="Project Name", max_length=50)
	status = models.CharField(max_length= 50) #status = models.ForeignKey(Status) Voir comment on fait des cleaned data avec des foreign keys dans un formulaire avec Django car lui il compare le text à l'id du status défini dans modèle status
	stage = models.CharField(max_length= 50)
	picture = models.ImageField(upload_to='picture/%Y/%m', blank=True, null=True)
	description = models.TextField(blank=True)
	project_leader = models.CharField(verbose_name="Project Leader", max_length=50)
	nbr_installations = models.IntegerField(verbose_name="Number of Installations", blank=True, null=True)
	power = models.IntegerField(verbose_name="Total Power (kW)", blank=True, null=True)
	start = models.DateField(verbose_name="Beginning of the project", auto_now_add=True, blank=True)
	#date_published = models.DateTimeField(auto_now=True)
	geom = models.PointField(srid=4326) #srid=4326 doit être la valeur par défaut je pense mais je l'écris quand même

	objects = models.GeoManager() # Allows to perform geoqueryset https://docs.djangoproject.com/en/1.7/ref/contrib/gis/model-api/#geomanager. Geoqueryset class : https://docs.djangoproject.com/en/1.7/ref/contrib/gis/geoquerysets/#django.contrib.gis.db.models.GeoQuerySet

	def __str__(self):
		return str(self.project_name)+' ('+str(self.project_leader)+')' # ou "{0} de {1}".format(self.project_name, self.project_leader)

	#def published_on_year_ago(self):
        #return self.date_published >= timezone.now() - datetime.timedelta(days=1)

	class Meta:
		verbose_name_plural = ugettext_lazy("Initiatives de projets méthanisation")
