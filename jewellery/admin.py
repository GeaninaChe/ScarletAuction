from django.contrib import admin
from .models import Jewellery


class JewelleryAdmin(admin.ModelAdmin):
    list_display = ("product_name", "description", "starting_price", "final_price")


admin.site.register(Jewellery, JewelleryAdmin)