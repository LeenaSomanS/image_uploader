from django.contrib import admin

# Register your models here.
from app.models import *
class UserAdmin(admin.ModelAdmin):
	list_display = ['user_id','full_name','user_name','password','image_hash_value','image_url']
admin.site.register(User,UserAdmin)