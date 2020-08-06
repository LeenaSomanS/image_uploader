from django.shortcuts import render
import json
from django.http import HttpResponse,JsonResponse
from app.models import *
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import hashlib
from django.core.files.storage import FileSystemStorage
import os
@csrf_exempt
def add_user_details(request):
    
    full_name=request.POST["fullName"]
    user_name=request.POST["userName"]
    password=request.POST["password"]
    thumbnail=request.FILES["thumbnail"]
    user_name_existence=User.objects.filter(user_name=user_name)
    if user_name_existence.count()!=0:
        return JsonResponse({"status":409,"message":"Email already exists"},safe=False)
    fs = FileSystemStorage()
    filename = fs.save(thumbnail.name, thumbnail)
    image_file = open("media/"+ filename,encoding="utf8", errors='ignore').read()
    image_hash_value=hashlib.md5(image_file .encode('utf-8')).hexdigest()
    hashed_pswd=hashlib.sha256(password.encode())
    hashed_pswd=hashed_pswd.hexdigest()
    user_object=User.objects.filter(image_hash_value=image_hash_value)
    _image_url=filename
    if user_object.count()!=0:
        _image_url=user_object[0].image_url
        os.remove("media/"+ filename)
    
    user_data=User(full_name=full_name,user_name=user_name,password=hashed_pswd,image_hash_value=image_hash_value,image_url=_image_url)
    user_data.save()
    return JsonResponse({"status":200,"message":"Successfully added"},safe=False)