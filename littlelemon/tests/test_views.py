from django.test import TestCase
from restaurant.views import MenuItemsView
from restaurant.models import MenuItem

class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = MenuItem(title="Salad", price=5.00, inventory=20)
        self.item2 = MenuItem(title="Pasta", price=10.00, inventory=10)
        self.item3 = MenuItem(title="Steak", price=25.00, inventory=10)
    
    def test_getAll(self):
        expected = [
            'Steak : 25.00',
            'Pasta : 10.00',
            'Salad : 5.00'
        ]
        i = 0
        items = MenuItem.objects.all()
        for item in items.iterator():
            self.assertEqual(item, expected[i])
            i += 1
