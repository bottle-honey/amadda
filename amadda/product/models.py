from django.db import models
from django.conf import settings
# Create your models here.

class Product(models.Model):
    product_id = models.IntegerField(unique=True, null=False, primary_key=True,verbose_name='상품 아이디')
    class Meta:
        verbose_name = '상품 정보'
        ordering = ['product_id',]
    # def __str__(self):
    #     return self.product_id