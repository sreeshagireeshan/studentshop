from django.db import models

# Create your models here.
class adminlogin_tb(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class addcategory_tb(models.Model):
    name=models.CharField(max_length=20)
