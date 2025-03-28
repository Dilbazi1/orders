from django.urls import path

from cafeapi import views
from cafeapi.apps import CafeapiConfig

app_name = CafeapiConfig.name
urlpatterns = [
    path("orders/", views.OrdersView.as_view(), name="orders"),
    path("orders/<int:pk>/", views.OrdersDetailView.as_view(), name="orders detail"),
    path("searchorder/", views.OrdersSearchView.as_view(), name="orders search"),
]
