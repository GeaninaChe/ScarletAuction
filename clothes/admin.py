from django.contrib import admin
from .models import Clothes


class ClothesAdmin(admin.ModelAdmin):
    list_display = ("product_name", "description", "starting_price", "final_price")


admin.site.register(Clothes, ClothesAdmin)