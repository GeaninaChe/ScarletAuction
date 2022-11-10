from django.db import models
from django.urls import reverse


# Create your models here.
class ArtObjects(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    starting_price = models.DecimalField(max_digits=6, decimal_places=2)
    current_price = models.DecimalField(max_digits=6, decimal_places=2)
    final_price = models.DecimalField(max_digits=6, decimal_places=2)

def __str__(self):
    return self.product_name

def get_absolute_url(self):
    return reverse('object_details', args=[str(self.id)])