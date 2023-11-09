from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def setUp(self):
        self.item = Menu.objects.create(name="Panini", price=15, inventory=100)

    def test_name(self):
        self.assertEqual(self.item.name, "Panini")

    def test_price(self):
        self.assertEqual(self.item.price, 15)

    def test_inventory(self):
        self.assertEqual(self.item.inventory, 100)