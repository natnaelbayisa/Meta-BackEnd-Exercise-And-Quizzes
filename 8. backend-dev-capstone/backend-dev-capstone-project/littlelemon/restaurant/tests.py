from django.test import TestCase
from restaurant.models import Menu

# Create your tests here.


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            name = "Kitfo",
            price = 1000,
            menu_item_description = "Its Ethiopian traditional food made up of chopped meat."
        )
        self.assertEqual(str(item), "Kitfo : 1000")
