from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = 'Monty Python administration'

my_admin_site = MyAdminSite(name='myadmin')