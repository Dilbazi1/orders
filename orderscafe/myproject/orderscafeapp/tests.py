from django.db.models import Q
from django.test import TestCase

from .models import Dish, Orders


class OrdersTestCase(TestCase):
    def setUp(self) -> None:
        dish = Dish.objects.create(name="eat1", price=89)
        order = Orders.objects.create(table_number=1)
        order.items.set([dish.id])
        order.save()

    def test_total_price(self) -> bool:
        order = Orders.objects.get(Q(table_number=1))
        self.assertEqual(order.total_price, None)
