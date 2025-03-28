from django.db.models import F, Sum

from orderscafeapp.models import Orders


def get_total_price(order: Orders) -> Orders:
    return Orders.objects.annotate(price=Sum(F("items__price"))).get(id=order.id)
