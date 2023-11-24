'''
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        # Test instances of Menu model
        Menu.objects.create(name='Cabbage Bites', price=10.50)
        Menu.objects.create(name='Soft Pretzel', price=8.00)
        Menu.objects.create(name='Dumplings', price=14.99)
        
    def test_getall(self):
        # Retrieve all Menu objects
        client = APIClient()
        url = reverse('menu-list')  # Adjust the URL pattern name based on your project
        response = client.get(url)

        # Check if the request was successful (status code 200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Serialize the retrieved objects
        menu_objects = Menu.objects.all()
        serializer = MenuSerializer(menu_objects, many=True)

        # Check if the serialized data equals the response data
        self.assertEqual(response.data, serializer.data)

'''