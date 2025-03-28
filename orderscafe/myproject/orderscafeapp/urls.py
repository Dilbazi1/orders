from django.urls import path

from orderscafeapp import views
from orderscafeapp.apps import OrderscafeappConfig

app_name = OrderscafeappConfig.name
urlpatterns = [
    path("orders-create/", views.OrderCreateView.as_view(), name="orders-create"),
    path("", views.IndexView.as_view(), name="index"),
    # path('<pk>/delete_items/', views.DeleteOrdersItemsView.as_view(),name='delete items'),
    # path('<int:pk>/delete_items/', views.delete_items,name='delete items'),
    path("<pk>/delete/", views.OrderDeleteView.as_view(), name="delete"),
    path("search-table-number/", views.SearchTableNumberView.as_view(), name="search"),
    path("<pk>/update-status/", views.UpdateOrderstatusView.as_view(), name="update-status"),
    path("<pk>/update-items/", views.UpdateOrdersItemsView.as_view(), name="update-items"),
    path("revenue/", views.RevenueView.as_view(), name="revenue"),
    path("<int:pk>/delete-func/", views.delete, name="delete-func"),
]
