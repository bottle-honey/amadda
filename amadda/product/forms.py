from django import forms
from .models import Product

# 상품추가 폼
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_price', 'product_stock', 'product_inf', 'product_site', 'product_imgloc',]