from django import forms

from .models import Orders


class OrderForm(forms.ModelForm):
    field_order = ["table_number", "items"]

    class Meta:
        model = Orders
        fields = ("table_number", "items")


class OrderItemForm(forms.ModelForm):
    field_order = ["items"]

    class Meta:
        model = Orders
        fields = ("items",)
