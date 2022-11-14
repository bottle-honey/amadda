from django.contrib import admin
from django.urls import path
from product.views import ProductListAPI

urlpatterns = [
    path('api/', ProductListAPI.as_view(), name='ProductListAPI')
]