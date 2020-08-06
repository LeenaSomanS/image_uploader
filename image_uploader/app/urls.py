from django.contrib import admin
from django.urls import path,include
from app.views import add_user_details
# from carts_app.views import *

urlpatterns = [
    path('api/add_user_details',add_user_details,name="add_user"),
] 