from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view()),
    path('categories/<int:pk>/', CategoryDetailUpdateDeleteView.as_view()),
    path('suppliers/', SupplierListCreateView.as_view()),
    path('suppliers/<int:pk>/', SupplierDetailUpdateDeleteView.as_view()),
    path('products/', ProductListCreateView.as_view()),
    path('products/<int:pk>/', ProductDetailUpdateDeleteView.as_view()),
    path('product-details/', ProductDetailListCreateView.as_view()),
    path('product-details/<int:pk>/', ProductDetailDetailUpdateDeleteView.as_view()),
    path('addresses/', AddressListCreateView.as_view()),
    path('addresses/<int:pk>/', AddressDetailUpdateDeleteView.as_view()),
    path('customers/', CustomerListCreateView.as_view()),
    path('customers/<int:pk>/', CustomerDetailUpdateDeleteView.as_view()),
    path('orders/', OrderListCreateView.as_view()),
    path('orders/<int:pk>/', OrderDetailUpdateDeleteView.as_view()),
    path('order-items/', OrderItemListCreateView.as_view()),
    path('order-items/<int:pk>/', OrderItemDetailUpdateDeleteView.as_view()),
]


