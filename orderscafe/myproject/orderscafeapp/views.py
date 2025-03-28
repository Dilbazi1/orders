from typing import Any

from django.db.models import Q, Sum
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from rest_framework.request import Request
from rest_framework.response import Response

from orderscafeapp.utils import get_total_price

from .forms import OrderForm, OrderItemForm
from .models import Orders


class IndexView(ListView):
    template_name = "index.html"
    model = Orders


class OrderCreateView(CreateView):
    template_name = "create_order.html"
    model = Orders
    form_class = OrderForm
    success_url = reverse_lazy("orderscafe:index")

    def form_valid(self, form: Any) -> Any:
        self.object = form.save()
        order = get_total_price(self.object)
        self.object.total_price = order.price
        return super().form_valid(form)


class OrderDeleteView(DeleteView):
    model = Orders
    success_url = reverse_lazy("orderscafe:index")
    template_name = "delete_orders.html"


class SearchTableNumberView(ListView):
    template_name = "search.html"
    model = Orders
    context_object_name = "all_search_results"

    def get_queryset(self) -> QuerySet:
        result = super(SearchTableNumberView, self).get_queryset()
        query = self.request.GET.get("search")
        if query:
            postresult = Orders.objects.filter(Q(table_number__contains=query) | Q(status__contains=query))
            result = postresult
        else:
            result = None
        return result


class UpdateOrderstatusView(UpdateView):
    model = Orders
    fields = ["status"]
    template_name = "update_order_status.html"
    success_url = reverse_lazy("orderscafe:index")


class UpdateOrdersItemsView(UpdateView):
    model = Orders
    # fields = ["items"]
    template_name = "update_order_items.html"
    success_url = reverse_lazy("orderscafe:index")
    form_class = OrderItemForm

    def form_valid(self, form: Any) -> Any:
        self.object = form.save()
        order = get_total_price(self.object)
        self.object.total_price = order.price
        return super().form_valid(form)


class RevenueView(ListView):
    model = Orders
    template_name = "revenue.html"
    context_object_name = "revenue"

    def get_queryset(self) -> QuerySet[Any]:
        orders = Orders.objects.filter(status="p").aggregate(Sum("total_price"))
        revenue = round(orders["total_price__sum"], 2)
        return revenue


def delete(request: Request, pk: int) -> Response:
    try:
        print(pk, type(pk))
        order = Orders.objects.get(pk=pk)
        order.delete()
    except Orders.DoesNotExist:
        return "Order with this id not found"
    return HttpResponseRedirect(reverse_lazy("orderscafe:index"))
