from django.db import models

# Create your models here.
class sellerlogin_tb(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class sellerregistration_tb(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    country=models.CharField(max_length=20,default=1)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    file=models.FileField()
    status=models.CharField(max_length=20,default="pending")

class addproduct_tb(models.Model):
    productname=models.CharField(max_length=20)
    details=models.CharField(max_length=20)
    price=models.IntegerField()
    stock=models.CharField(max_length=20)
    file=models.FileField()
    categoryid=models.ForeignKey('siteadmin.addcategory_tb',on_delete=models.CASCADE)
    sellerid=models.ForeignKey('sellerregistration_tb',on_delete=models.CASCADE)

class trackorder_tb(models.Model):
    orderid=models.ForeignKey('buyer.buyerorder_tb',on_delete=models.CASCADE)
    detail=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)



