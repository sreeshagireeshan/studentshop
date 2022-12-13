from django.shortcuts import render,redirect
from buyer.models import *
from siteadmin.models import *
from seller.models import *
from django.contrib import messages
import datetime
# Create your views here.
def buyerregistration(request):
    return render(request,"buyerregistration.html")

def registerAction(request):
    name=request.POST['name']
    address=request.POST['address']
    phone=request.POST['phone']
    gender=request.POST['gender']
    dob=request.POST['dob']
    country=request.POST['country']
    username=request.POST['username']
    password=request.POST['password']
    user=buyerregistration_tb(name=name,address=address,phone=phone,gender=gender,dob=dob,country=country,username=username,password=password)
    user.save()
    messages.add_message(request,messages.INFO,"Registration Successfull")
    return redirect('buyerregistration')

def updatebuyerprofile(request):
    buyerid=request.session['buyerid']
    buyer=buyerregistration_tb.objects.filter(id=buyerid)
    return render(request,"updatebuyerprofile.html",{"buyer":buyer})

def updateAction(request):
    buyerid=request.POST['id']
    name=request.POST['name']
    address=request.POST['address']
    gender=request.POST['gender']
    dob=request.POST['dob']
    phone=request.POST['phone']
    country=request.POST['country']
    username=request.POST['username']
    password=request.POST['password']
    buyer=buyerregistration_tb.objects.filter(id=buyerid).update(name=name,address=address,gender=gender,dob=dob,phone=phone,country=country,username=username,password=password)
    messages.add_message(request,messages.INFO,"updated Successfully")
    return redirect("updatebuyerprofile")

def viewselleraddedproducts(request):
    buyerid=request.session['buyerid']
    buyer=addproduct_tb.objects.all()
    return render(request,"viewselleraddedproducts.html",{'buyer':buyer})

def addtocart(request,productid):
    product=addproduct_tb.objects.filter(id=productid)
    return render(request,"addtocart.html",{'product':product})

def buynowAction(request):
    buyerid=request.session['buyerid']
    productid=request.POST['id']
    shippingaddress=request.POST['shippingaddress']
    contactnumber=request.POST['contactnumber']
    quantity=request.POST['quantity']
    totalprice=request.POST['totalprice']
    cart=addtocart_tb(shippingaddress=shippingaddress,contactnumber=contactnumber,quantity=quantity,totalprice=totalprice,buyerid_id=buyerid,productid_id=productid)
    cart.save()
    messages.add_message(request,messages.INFO,"Successfull")
    return redirect("viewselleraddedproducts")

def viewcart(request):
    buyerid=request.session['buyerid']
    cartview=addtocart_tb.objects.filter(buyerid=buyerid)
    return render(request,"viewcart.html",{'cartview':cartview})

def cartdelete(request,id):
    kart=addtocart_tb.objects.filter(id=id).delete()
    return redirect("viewcart")

def placetheorderAction(request):
    cartitems=request.POST.getlist('checkbox')
    date=datetime.date.today()
    time=datetime.datetime.now().strftime('%H:%M')
    for cid in cartitems:
        cart1=addtocart_tb.objects.filter(id=cid)
        shippingaddress=cart1[0].shippingaddress
        quantity=cart1[0].quantity
        stock=cart1[0].productid.stock
        contactnumber=cart1[0].contactnumber
        totalprice=cart1[0].totalprice
        productid=cart1[0].productid
        buyerid=request.session['buyerid']
        sellerid=cart1[0].productid.sellerid
        if quantity>int(stock):
            messages.add_message(request,messages.INFO,"quantity greater than stock")
            return redirect("viewcart")
        else:
            cart2=buyerorder_tb(shippingaddress=shippingaddress,quantity=quantity,contactnumber=contactnumber,totalprice=totalprice,sellerid=sellerid,buyerid_id=buyerid,productid=productid,date=date,time=time)
            cart2.save()
            newstock=int(stock)-quantity
            product=addproduct_tb.objects.filter(id=productid.id).update(stock=newstock)
            cart1.delete()
            messages.add_message(request,messages.INFO," order Successfull")
    return redirect("viewcart")

def myorders(request):
    buyer=request.session['buyerid']
    order= buyerorder_tb.objects.filter(buyerid=buyer)
    return render(request,"myorders.html",{'orders':order})

def cancel(request,id):
    order1=buyerorder_tb.objects.filter(id=id).update(status="cancelled")
    return redirect("myorders")

def trackmyorder(request,id):
    myorder=trackorder_tb.objects.filter(orderid_id=id)
    return render(request,"trackmyorder.html",{'myorder1':myorder})

def searchproduct(request):
    return render(request,"searchproduct.html")

def productsearchAction(request):
    productname=request.POST['productname']
    search=addproduct_tb.objects.filter(productname__istartswith=productname)
    return render(request,"viewselleraddedproducts.html",{'buyer':search})

def searchcategory(request):
    category=addcategory_tb.objects.all()
    return render(request,"searchcategory.html",{'category1':category})

def searchcategoryAction(request):
    category=request.POST['category']
    price=request.POST['price']
    action1=addproduct_tb.objects.filter(price__lte=price,categoryid=category)
    return render(request,"viewselleraddedproducts.html",{'buyer':action1})
    




