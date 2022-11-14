from django.db import models
from django.urls import reverse


class ArtObjects(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    starting_price = models.CharField(max_length=10)
    final_price = models.CharField(max_length=10)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('object_details', args=[str(self.id)])