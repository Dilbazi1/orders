from typing import Any

from rest_framework import generics, status
from rest_framework.filters import SearchFilter
from rest_framework.request import Request
from rest_framework.response import Response

from orderscafeapp.models import Orders
from orderscafeapp.utils import get_total_price

from .serializers import OrdersSerializer


class OrdersView(generics.ListCreateAPIView):
    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()

    def post(self, request: Request, format: Any = None) -> Response:
        serializer = OrdersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        order = get_total_price(order)
        order.total_price = order.price
        order = order.save()
        return Response(
            status=status.HTTP_201_CREATED,
        )


class OrdersDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()


class OrdersSearchView(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    filter_backends = [SearchFilter]
    search_fields = ["table_number", "status"]
