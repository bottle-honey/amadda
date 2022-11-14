from django.contrib import admin
from django.urls import path
from product.views import ProductListAPI
from . import views
urlpatterns = [
    path('api/', ProductListAPI.as_view(), name='ProductListAPI'),
    path('create_postform/', views.Product_post, name='create_postform'),
    path('product_list/', views.product_list ,name='product_list' ),
    path('product_add/', views.product_add ,name='product_add' ),

]