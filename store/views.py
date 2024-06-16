from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import *

from .serializers import *


class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SupplierListCreateView(ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer  # Использование другого сериализатора для GET-запросов
        return ProductCreateUpdateSerializer


class ProductDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer  # Использование другого сериализатора для GET-запросов
        return ProductCreateUpdateSerializer


class ProductDetailListCreateView(ListCreateAPIView):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductDetailSerializer  # Использование другого сериализатора для GET-запросов
        return ProductDetailCreateUpdateSerializer


class ProductDetailDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductDetailSerializer  # Использование другого сериализатора для GET-запросов
        return ProductDetailCreateUpdateSerializer


class AddressListCreateView(ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class CustomerListCreateView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CustomerSerializer  # Использование другого сериализатора для GET-запросов
        return CustomerCreateUpdateSerializer


class CustomerDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerCreateUpdateSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CustomerSerializer  # Использование другого сериализатора для GET-запросов
        return CustomerCreateUpdateSerializer


class OrderListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderSerializer  # Использование другого сериализатора для GET-запросов
        return OrderCreateUpdateSerializer


class OrderDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderSerializer  # Использование другого сериализатора для GET-запросов
        return OrderCreateUpdateSerializer


class OrderItemListCreateView(ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderItemSerializer  # Использование другого сериализатора для GET-запросов
        return OrderItemCreateUpdateSerializer


class OrderItemDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderItemSerializer  # Использование другого сериализатора для GET-запросов
        return OrderItemCreateUpdateSerializer


