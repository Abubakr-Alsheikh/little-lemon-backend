from django.test import TestCase, Client
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.response import Response

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        Menu.objects.create(Title="Cake", Price=100, Inventory=100)
        self.client = Client()

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        menu_items = Menu.objects.all()
        serialized_data = MenuSerializer(menu_items, many=True).data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serialized_data)