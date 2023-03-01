from django.test import TestCase
from restaurant.models import Menu


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            name="Kitfo",
            price= 1000,
             menu_item_description = "It's delicious"
        )
        self.assertEqual(str(item), "Kitfo : 1000")
