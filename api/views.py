from django.shortcuts import render

# imports
from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView, RetrieveAPIView, ListAPIView, CreateAPIView

from .serializers import ProductSerializer , CategorySerializer

from products.models import Product , Category

from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework import parsers, renderers
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


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
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    

class ProductApiView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductCreate(CreateAPIView):
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


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    if coreapi_schema.is_enabled():
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="username",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Username",
                        description="Valid username for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


obtain_auth_token = ObtainAuthToken.as_view()