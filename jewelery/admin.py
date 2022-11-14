from django.contrib import admin
from .models import Jewelery


class JeweleryAdmin(admin.ModelAdmin):
    list_display = ("product_name", "description", "starting_price", "final_price")


admin.site.register(JeweleryAdmin, JeweleryAdmin)