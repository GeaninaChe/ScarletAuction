from django.db import models


# Create your models here.
class ArtObjects(models.Model):
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    starting_price = models.DecimalField(max_digits=6, decimal_places=2)
    final_price = models.DecimalField(max_digits=6, decimal_places=2)

def __str__(self):
    return self.product_name