from django.shortcuts import render

# imports
from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView, RetrieveAPIView, ListAPIView

from .serializers import ProductSerializer , CategorySerializer

from products.models import Product , Category

from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


# views
class CategoryApiView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    # def list(self, request):
    #     # Get the queryset and serialize it.
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True)

    #     # Extract the ID and name of each category item and add them to a new list.
    #     categories = []
    #     for item in serializer.data:
    #         categories.append({'id': item['id'], 'name': item['name']})

    #     # Return the list of categories as a JSON response.
    #     return JsonResponse(categories, safe=False)\


class CategoryUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    

class ProductApiView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


# class ProductCategoryRetrieve(RetrieveAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()
#     lookup_field = 'category'
#     lookup_url_kwarg = 'category'


class ProductCategoryRetrieve(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        category = self.kwargs.get('category')
        obj = get_object_or_404(queryset, category=category)
        return obj