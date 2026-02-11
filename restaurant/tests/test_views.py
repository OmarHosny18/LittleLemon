from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from ..models import Menu
from ..serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test Menu instances
        self.menu1 = Menu.objects.create(title="Pizza", price=10.99, inventory=50)
        self.menu2 = Menu.objects.create(title="Burger", price=7.99, inventory=30)
        self.menu3 = Menu.objects.create(title="Pasta", price=12.50, inventory=20)

        # APIClient instance
        self.client = APIClient()

        # URL for the menu list view
        self.list_url = reverse('menuitem-list')  # Must match the name in urls.py
        self.detail_url = lambda pk: reverse('single-menuitem', kwargs={'pk': pk})

    def test_get_all_menu_items(self):
        # Send GET request to list all menu items
        response = self.client.get(self.list_url)
        
        # Serialize DB objects
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        
        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_single_menu_item(self):
        # Pick a menu item to retrieve
        menu = self.menu1
        url = self.detail_url(menu.pk)
        
        # Send GET request for a single menu item
        response = self.client.get(url)
        
        # Serialize the object
        serializer = MenuSerializer(menu)
        
        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
