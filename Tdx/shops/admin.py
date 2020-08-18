from django.contrib import admin

from django.contrib.gis.admin import OSMGeoAdmin
from .models import Shop, Company


@admin.register(Shop)
@admin.register(Company)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name',)


# class CompanyAdmin():
#     list_display('name',)
