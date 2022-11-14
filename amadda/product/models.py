from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Product(models.Model):
    product_id = models.IntegerField(unique=True, null=False, primary_key=True,verbose_name='상품 아이디')
    category_id = models.IntegerField(default=0, verbose_name='상품 카테고리 아이디')
    product_price = models.IntegerField(null=False, verbose_name='상품 가격')
    product_name = models.CharField(max_length=100, null=False, verbose_name='상품 이름')
    product_inf = models.TextField(null=False, verbose_name='상품 설명')
    product_stock = models.IntegerField(default=0,null=False, verbose_name='상품 재고')
    product_sold = models.IntegerField(default=0,null=False,verbose_name='상품 판매량')
    # product_enroll = models.DateTimeField(auto_now_add=True,default=timezone.now(),verbose_name='상품 등록일')
    product_site = models.CharField(max_length=300,null=True,verbose_name='상품 판매 사이트')
    product_sale = models.IntegerField(default=0,null=False,verbose_name='상품 할인 퍼센트')
    class Meta:
        verbose_name = '상품 정보'
        ordering = ['product_name',]
    def __str__(self):
        return self.product_name