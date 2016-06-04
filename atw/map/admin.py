#-*- coding: utf-8 -*-

from django.contrib.gis import admin # AdminSite ModelAdmin OSMGeoAdmin sont compris dans le gis.admin dont je comprend pas pourquoi je dois les charger ensuite...
from leaflet.admin import LeafletGeoAdmin
from .models import TripStage, Massif, Type, Trip
from django.contrib.gis.geos import Point

#class TripInline(admin.TabularInline):
    #model = Trip.stages.through

class TripStageInline(admin.TabularInline):
    model = TripStage.trips.through
    extra = 1


class TripStageAdmin(LeafletGeoAdmin): # avant leafletgeoadmin je faisais hériter de admin.OSMGeoAdmin (OSMGeoAdmin hérite de GeoModelAdmin qui hérite de ModelAdmin)
    fieldsets = [
        ('Mandatory information', {'fields': ['date_published', 'geom', 'stage_name', 'trips', 'date', 'massif', 'type']}),
        ('Optional information',  {'fields': ['picture_tag', 'display_picture_tag', 'story', 'distance', 'duration'], 'classes': ['collapse']}),
        ('Publication information', {'fields': ['added_by', 'email_validation', 'email'], 'classes': ['collapse']}),
    ]
    #inlines = [TripInline]
    list_display = ('stage_name', 'massif', 'date', 'distance', 'published_more_than_6_months_ago', 'display_picture_tag', 'added_by')
    list_editable = ['date', 'massif', 'distance']
    readonly_fields = ['date_published', 'display_picture_tag', 'added_by'] # https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#django.contrib.admin.ModelAdmin.readonly_fields
    search_fields = ['stage_name']
    list_filter = ['massif', 'added_by']
    save_on_top = True
    #map_width = 900 # Ne marche pas avec Leaflet

    #pt = Point(4.85, 45.75, srid=4326)
    #pt.transform(3857)
    #default_lon, default_lat = pt.coords

class TripAdmin(LeafletGeoAdmin):
    fieldsets = [
        (None, {'fields': ['date_published', 'geom', 'trip_name', 'start_date', 'end_date', 'picture_tag', 'display_picture_tag']}),
    ]
    inlines = [TripStageInline]
    list_display = ('trip_name', 'start_date', 'end_date')
    list_editable = ['start_date', 'end_date']
    search_fields = ['trip_name']
    readonly_fields = ['date_published', 'display_picture_tag']

admin.site.register(TripStage, TripStageAdmin)
admin.site.register(Massif)
admin.site.register(Type)
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
