from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.views import Menu
from django.core.serializers import serialize


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=300, inventory=50)

    def test_get_all(self):
        client = APIClient()
        response = client.get("/restaurant/menu/")
        expected_data = serialize('json', Menu.objects.all(), fields=('title', 'price', 'inventory'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
