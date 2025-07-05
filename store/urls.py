from django.urls import path
from .views import ProductCreateView, ProductSearchView, add_to_cart, cart_view, confirm_order

urlpatterns = [
    path('add-product/', ProductCreateView.as_view(), name='add-product'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add-to-cart'),
    path('cart/', cart_view, name='cart'),
    path('confirm-order/', confirm_order, name='confirm-order'),
    path('search/', ProductSearchView.as_view(), name='product-search'),
]