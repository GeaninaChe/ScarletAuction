from django.test import Client, TestCase
from django.urls import reverse

import artobjects
from .models import Car


class CarTest(TestCase):
    def setUp(self):
        self.artobjects = Car.objects.create(
            product_name='',
            description='',
            starting_price='',
            final_price='', )

    def test_car_listing(self):
        self.assertEqual(f'{self.car.product_name}', '')
        self.assertEqual(f'{self.car.description}', '')
        self.assertEqual(f'{self.car.starting_price}', '')
        self.assertEqual(f'{self.car.final_price}', '')

    def test_car_list_view(self):
        response = self.client.get(reverse('cars_listt'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '')
        self.assertTemplateUsed(response, 'cars/update_car.html')

    def test_car_details_view(self):
        response = self.client.get(self.car.get_absolute_url())
        no_response = self.client.get('/cars/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'é')
        self.assertTemplateUsed(response, 'cars/car_details.html')
