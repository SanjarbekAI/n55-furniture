from django.urls import path

from app_orders.views import add_or_remove_cart

app_name = "orders"

urlpatterns = [
    path('cart/add-or-remove/<int:pk>/', add_or_remove_cart, name='add-or-remove-cart'),
    # path('wishlist/add-or-remove/<int:pk>/', add_or_remove_wishlist, name='add-or-remove-wishlist'),
]