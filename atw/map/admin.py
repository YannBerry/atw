from django.contrib.gis import admin # AdminSite ModelAdmin OSMGeoAdmin sont compris dans le gis.admin dont je comprend pas pourquoi je dois les charger ensuite...
from leaflet.admin import LeafletGeoAdmin
from .models import Initiative, Status, Stage
from django.contrib.gis.geos import Point

class InitiativeAdmin(LeafletGeoAdmin): # avant leafletgeoadmin je faisais hérité de admin.OSMGeoAdmin. Même si je touche à list_display, search..., list...pas besoin de faire hériter également de la classe ModelAdmin car OSMGeoAdmin hérite déjà de GeoModelAdmin qui hérite de ModelAdmin
	list_display = ('project_name', 'stage', 'status', 'power')
	search_fields = ['project_name']
	list_filter = ['power']
	save_on_top = True
	#map_width = 900 # Ne marche pas avec Leaflet
	
	#pt = Point(4.85, 45.75, srid=4326)
	#pt.transform(3857)
	#default_lon, default_lat = pt.coords

admin.site.register(Initiative, InitiativeAdmin)
admin.site.register(Status)
admin.site.register(Stage)

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