from django.contrib import admin
from .models import Wine, Region, Winery, Grape

admin.site.register(Wine)
admin.site.register(Region)
admin.site.register(Winery)
admin.site.register(Grape)

