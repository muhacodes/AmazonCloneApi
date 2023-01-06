"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import (
    ProductApiView,
    CategoryApiView,
    ProductUpdateDeleteApiView,
    ProductCategoryRetrieve,
    ProductCategoryRetrieve,
    CategoryUpdateDeleteApiView
)

urlpatterns = [

    # get or post a category
    path('category', CategoryApiView.as_view(),),

    path('category/<int:pk>', CategoryUpdateDeleteApiView.as_view(),),

    # Methods ['get', 'post'] for products
    path('product', ProductApiView.as_view(),),

    # retrieve product
    path('product/<int:pk>', ProductUpdateDeleteApiView.as_view(),),

    path('product/category/<int:category>/', ProductCategoryRetrieve.as_view(), name='product-category-detail'),

    # path('product/category/<int:pk>', ProductCategoryRetrieve.as_view(),),

    # deelte product
    path('product/delete/<int:pk>', ProductUpdateDeleteApiView.as_view(),),

]
