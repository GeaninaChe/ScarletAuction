from django.contrib import admin
from .models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ("product_name", "description", "starting_price", "final_price")


admin.site.register(Car, CarAdmin)