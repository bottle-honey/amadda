from django.db import models
from django.conf import settings
# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=30, unique=True, null=False, primary_key=True,verbose_name='유저 아이디')
    user_password = models.CharField(max_length=30,  null=True, verbose_name='유저 비밀번호')
    user_email = models.EmailField(max_length=128, null=True, verbose_name='유저 이메일')
    user_phone = models.CharField(max_length=13, null=True, verbose_name='유저 전화번호')
    user_address = models.CharField(max_length= 300,  null=True, verbose_name='유저 집주소')
    user_register_dttm = models.DateTimeField(auto_now_add=True,  null=True, verbose_name='계정 생성시간')

    class Meta:
        verbose_name = '유저 정보'
        ordering = ['user_register_dttm',]
    def __str__(self):
        return self.user_id