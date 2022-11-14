# Generated by Django 4.1.3 on 2022-11-14 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_product_imgloc_product_product_uploaddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_imgloc',
            field=models.FileField(blank=True, upload_to='img/%y/%m/%d/', verbose_name='이미지파일위치'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_uploaddate',
            field=models.DateField(auto_now=True, verbose_name='이미지 업로드 날짜'),
        ),
    ]