from django.test import TestCase
from django.urls import reverse
from restaurant.models import Menu
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.serializers import MenuSerializer
from restaurant.views import MenuItemView
class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(Title='IceCream', Price=80, Inventory=100)
        Menu.objects.create(Title='Pizza', Price=12, Inventory=50)

    def test_getall(self):

        url = reverse(MenuItemView.as_view())  
        client = APIClient()
        response = client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        menu_objects = Menu.objects.all()
        serializer = MenuSerializer(menu_objects, many=True)

        self.assertEqual(response.data, serializer.data)
