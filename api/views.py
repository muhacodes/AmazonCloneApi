from django.shortcuts import render

# Create your views here.
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .serializers import (
    ProductSerializer,
    CategorySerializer
)
from products.models import (
    Product,
    Category
)


class CategoryApiView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductApiView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
