from django.contrib import admin
from .models import Wine, Region, Winery, Grape, WineType


class WineAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'friendly_name',
        'wine_type',
        'price',
        'winery',
    )

    ordering = ('sku',)

class WineryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )

class RegionAdmin(admin.ModelAdmin):
        list_display = (
        'name',
        'friendly_name',
    )

class GrapeAdmin(admin.ModelAdmin):
        list_display = (
        'name',
        'friendly_name',
    )

class WineTypeAdmin(admin.ModelAdmin):
        list_display = (
        'name',
        'friendly_name',
    )

admin.site.register(Wine, WineAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Winery, WineryAdmin)
admin.site.register(Grape, GrapeAdmin)
admin.site.register(WineType, WineTypeAdmin)
