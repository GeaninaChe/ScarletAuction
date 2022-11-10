from django.contrib import admin
from .models import ArtObjects

class ArtObjectsAdmin(admin.ModelAdmin):
    list_display = ("product_name", "description", "starting_price", "current_price", "final_price")


admin.site.register(ArtObjects, ArtObjectsAdmin)