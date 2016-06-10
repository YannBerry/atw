#-*- coding: utf-8 -*-

from django.contrib.gis import admin # AdminSite ModelAdmin OSMGeoAdmin sont compris dans le gis.admin dont je comprend pas pourquoi je dois les charger ensuite...
from leaflet.admin import LeafletGeoAdmin
from .models import TripStage, Massif, Type, Trip, Country
from django.contrib.gis.geos import Point

#class TripStageInline(admin.TabularInline):
    #model = TripStage.trips.through
    #extra = 1


class TripStageAdmin(LeafletGeoAdmin): # avant leafletgeoadmin je faisais hériter de admin.OSMGeoAdmin (OSMGeoAdmin hérite de GeoModelAdmin qui hérite de ModelAdmin)
    fieldsets = [
        ('Mandatory information', {'fields': ['date_published', 'geom', 'stage_name_fr', 'stage_name_en', 'stage_slug_fr', 'stage_slug_en', 'country', 'trip_linked', 'date', 'massif', 'type']}),
        ('Optional information',  {'fields': ['picture_tag', 'display_picture_tag', 'story_fr', 'story_en', 'distance', 'duration'], 'classes': ['collapse']}),
        ('Publication information', {'fields': ['added_by', 'email_validation', 'email'], 'classes': ['collapse']}),
    ]
    list_display = ('stage_name', 'stage_slug', 'date', 'distance', 'published_more_than_6_months_ago', 'added_by')
    list_editable = ['stage_slug', 'date', 'distance']
    readonly_fields = ['date_published', 'display_picture_tag', 'added_by'] # https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#django.contrib.admin.ModelAdmin.readonly_fields
    prepopulated_fields = {"stage_slug_fr": ("stage_name_fr",), "stage_slug_en": ("stage_name_en",)}
    search_fields = ['stage_name']
    list_filter = ['massif', 'added_by']
    save_on_top = True
    #map_width = 900 # Ne marche pas avec Leaflet

    #pt = Point(4.85, 45.75, srid=4326)
    #pt.transform(3857)
    #default_lon, default_lat = pt.coords

class TripAdmin(LeafletGeoAdmin):
    fieldsets = [
        (None, {'fields': ['date_published', 'geom', 'trip_name_fr', 'trip_name_en', 'trip_slug_fr', 'trip_slug_en', 'start_date', 'end_date', 'nbr_of_days', 'description_fr', 'description_en', 'picture_tag', 'display_picture_tag']}),
    ]
    #inlines = [TripStageInline]
    list_display = ('trip_name', 'trip_slug', 'start_date', 'end_date', 'nbr_of_days')
    list_editable = ['start_date', 'trip_slug', 'end_date']
    prepopulated_fields = {"trip_slug_fr": ("trip_name_fr",), "trip_slug_en": ("trip_name_en",)}
    search_fields = ['trip_name']
    readonly_fields = ['date_published', 'nbr_of_days', 'display_picture_tag']

admin.site.register(TripStage, TripStageAdmin)
admin.site.register(Massif)
admin.site.register(Type)
admin.site.register(Country)
admin.site.register(Trip, TripAdmin)


# from django.contrib.gis import admin # AdminSite ModelAdmin OSMGeoAdmin sont compris dans le gis.admin dont je comprend pas pourquoi je dois les charger ensuite...
# from django.contrib import admin
# from .models import Initiative, Status
# from django.contrib.gis.geos import Point

# class MyAdminSite(admin.AdminSite):
# 	site_header = 'AD Around The World Administration'

# admin_site = MyAdminSite()

# @admin.register(Initiative, site=MyAdminSite)# Utilise le design pattern "decorator" au lieu d'ajouter la ligne admin_site.register(Initiative, InitiativeAdmin) après la définition de la classe InitiativeAdmin
# class InitiativeAdmin(admin.OSMGeoAdmin): # même si je touche à list_display, search..., list...pas besoin de faire hériter également de la classe ModelAdmin car OSMGeoAdmin hérite déjà de GeoModelAdmin qui hérite de ModelAdmin
# 	list_display = ('project_name', 'status', 'power')
# 	search_fields = ['project_name']
# 	list_filter = ['power']
# 	save_on_top = True
# 	map_width = 900
	
# 	pt = Point(4.85, 45.75, srid=4326)
# 	pt.transform(3857)
# 	default_lon, default_lat = pt.coords

# @admin.register(Status, Initiative, site=MyAdminSite) # au lieu de admin_site.register(Status)
# class StatusAdmin(admin.ModelAdmin):
#     pass
