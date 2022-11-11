from django.contrib import admin
from accounts.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id','user_register_dttm')

admin.site.register(User, UserAdmin)