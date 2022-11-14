# Generated by Django 4.1.3 on 2022-11-14 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='상품 아이디')),
                ('category_id', models.IntegerField(default=0, verbose_name='상품 카테고리 아이디')),
                ('product_price', models.IntegerField(verbose_name='상품 가격')),
                ('product_name', models.CharField(max_length=100, verbose_name='상품 이름')),
                ('product_inf', models.TextField(verbose_name='상품 설명')),
                ('product_stock', models.IntegerField(default=0, verbose_name='상품 재고')),
                ('product_sold', models.IntegerField(default=0, verbose_name='상품 판매량')),
                ('product_enroll', models.DateTimeField(auto_now_add=True, null=True, verbose_name='상품 등록일')),
                ('product_site', models.CharField(max_length=300, null=True, verbose_name='상품 판매 사이트')),
                ('product_sale', models.IntegerField(default=0, verbose_name='상품 할인 퍼센트')),
            ],
            options={
                'verbose_name': '상품 정보',
                'ordering': ['product_name'],
            },
        ),
    ]
