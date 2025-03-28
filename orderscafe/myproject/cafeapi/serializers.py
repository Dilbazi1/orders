from typing import Any

from rest_framework import serializers

from orderscafeapp.models import Dish, Orders
from orderscafeapp.utils import get_total_price


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = "__all__"


class OrdersSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    items = serializers.PrimaryKeyRelatedField(many=True, queryset=Dish.objects.all())

    class Meta:
        model = Orders
        fields = ["id", "table_number", "items", "total_price", "status"]

    def get_total_price(self, obj: Any) -> float:
        total_price = get_total_price(obj)
        return total_price.price
