from django.db import models

# Create your models here.
class buyerregistration_tb(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    country=models.CharField(max_length=20,default=1)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class addtocart_tb(models.Model):
    productid=models.ForeignKey('seller.addproduct_tb',on_delete=models.CASCADE)
    buyerid=models.ForeignKey('buyerregistration_tb',on_delete=models.CASCADE)
    shippingaddress=models.CharField(max_length=20)
    contactnumber=models.CharField(max_length=20)
    quantity=models.IntegerField()
    totalprice=models.IntegerField()

class buyerorder_tb(models.Model):
    sellerid=models.ForeignKey('seller.sellerregistration_tb',on_delete=models.CASCADE)
    productid=models.ForeignKey('seller.addproduct_tb',on_delete=models.CASCADE)
    buyerid=models.ForeignKey('buyerregistration_tb',on_delete=models.CASCADE)
    shippingaddress=models.CharField(max_length=20)
    contactnumber=models.CharField(max_length=20)
    quantity=models.IntegerField()
    totalprice=models.IntegerField()
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    status=models.CharField(max_length=20,default='pending')
    
    

    
