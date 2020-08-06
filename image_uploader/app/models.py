from django.db import models

# Create your models here.
class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    full_name= models.CharField(max_length=100)
    user_name= models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    image_hash_value= models.CharField(max_length=1000)
    image_url= models.CharField(max_length=500)