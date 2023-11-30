from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_instance(self):
        item = Menu(Title = 'IceCream',Price = 80, Inventory = 100)
        expected_representation = "IceCream:80"
        self.assertEqual(str(item), expected_representation)