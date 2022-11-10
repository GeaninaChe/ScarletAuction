from django.test import Client, TestCase
from django.urls import reverse

import artobjects
from .models import ArtObjects


class ArtObjectsTest(TestCase):
    def setUp(self):
        self.artobjects = ArtObjects.objects.create(
            product_name='Mickey étonné',
            description='Acrylic on canvas,100×2.5×81 cm',
            starting_price='65.99',
            current_price='110.00',
            final_price='300.00', )


    def test_artobjects_listing(self):
        self.assertEqual(f'{self.artobjects.product_name}', 'Mickey étonné')
        self.assertEqual(f'{self.artobjects.description}', 'Acrylic on canvas,100×2.5×81 cm')
        self.assertEqual(f'{self.artobjects.starting_price}', '65.99')
        self.assertEqual(f'{self.artobjects.current_price}', '110.00')
        self.assertEqual(f'{self.artobjects.current_price}', '300.00')


    def test_objects_list_view(self):
        response = self.client.get(reverse('objects_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Mickey étonné')
        self.assertTemplateUsed(response, 'artobjects/objects_list.html')


    def test_object_details_view(self):
        response = self.client.get(self.artobjects.get_absolute_url())
        no_response = self.client.get('/artobjects/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Mickey étonné')
        self.assertTemplateUsed(response, 'artobjects/object_details.html')
