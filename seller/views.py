from django.shortcuts import render,redirect
from seller.models import *
from siteadmin.models import *
from buyer.models import *
from django.contrib import messages
import datetime
# Create your views here.
def sellerregistration(request):
    return render(request,"sellerregistration.html")

def sellerregisterAction(request):
    name=request.POST['name']
    address=request.POST['address']
    phone=request.POST['phone']
    gender=request.POST['gender']
    dob=request.POST['dob']
    country=request.POST['country']
    username=request.POST['username']
    password=request.POST['password']
    if len(request.FILES)>0:
        file=request.FILES['file']
    else:
        file="no pic"
    user=sellerregistration_tb(name=name,address=address,phone=phone,gender=gender,dob=dob,country=country,username=username,password=password,file=file)
    user.save()
    messages.add_message(request,messages.INFO,"Registration Successfull")
    return redirect('sellerregistration')

def updatesellerprofile(request):
    sellerid=request.session['sellerid']
    seller=sellerregistration_tb.objects.filter(id=sellerid)
    return render(request,"updatesellerprofile.html",{"seller":seller})

def updatesellerAction(request):
    sellerid=request.session['sellerid']
    seller=sellerregistration_tb.objects.filter(id=sellerid)
    name=request.POST['name']
    address=request.POST['address']
    gender=request.POST['gender']
    dob=request.POST['dob']
    phone=request.POST['phone']
    country=request.POST['country']
    username=request.POST['username']
    password=request.POST['password'] 
    if len(request.FILES)>0:
        file=request.FILES['file']
    else:
        file=seller[0].file
        #file1=request.POST['file']
        #file=file1
     
    seller=sellerregistration_tb.objects.filter(id=sellerid).update(name=name,address=address,gender=gender,dob=dob,phone=phone,country=country,username=username,password=password)
    seller_object=sellerregistration_tb.objects.get(id=sellerid)
    seller_object.file=file
    seller_object.save()
    messages.add_message(request,messages.INFO,"updated successfully")
    return redirect("updatesellerprofile")

def addproduct(request):
    sellerid=request.session['sellerid']
    product=addcategory_tb.objects.all()
    return render(request,"addproduct.html",{'product':product})

def addproductAction(request):
    sellerid=request.session['sellerid']
    productname=request.POST['productname']
    details=request.POST['details']
    price=request.POST['price']
    stock=request.POST['stock']
    if len(request.FILES)>0:
        file=request.FILES['file']
    else:
        file="no pic"
    category=request.POST['category']
    seller=addproduct_tb(productname=productname,details=details,price=price,stock=stock,categoryid_id=category,sellerid_id=sellerid,file=file)
    seller.save()
    messages.add_message(request,messages.INFO,"successful")
    return redirect("addproduct")

def viewaddproduct(request):
    seller=request.session['sellerid']
    user=addproduct_tb.objects.filter(sellerid=seller)
    return render(request,"viewaddproduct.html",{'user':user})

def delete(request,id):
    seller=addproduct_tb.objects.filter(id=id).delete()
    return redirect("viewaddproduct")

def edit(request,id):
    seller=addproduct_tb.objects.filter(id=id)
    category=addcategory_tb.objects.all()
    return render(request,"edit.html",{'seller':seller,'category':category})

def editupdateAction(request):
    sellerid=request.session['sellerid']
    productid=request.POST['id']
    product=addproduct_tb.objects.filter(id=productid)
    productname=request.POST['productname']
    details=request.POST['details']
    price=request.POST['price']
    stock=request.POST['stock']
    if len(request.FILES)>0:
        file=request.FILES['file']
    else:
        file= product[0].file
    category=request.POST['category']
    product=addproduct_tb.objects.filter(id= productid).update(productname=productname,details=details,price=price,stock=stock,categoryid_id=category,sellerid_id=sellerid,file=file)
    product_object=addproduct_tb.objects.get(id= productid)
    product_object.file=file
    product_object.save()
    messages.add_message(request,messages.INFO,"successful")
    return redirect("viewaddproduct")

def viewcustomerorders(request):
    seller=request.session['sellerid']
    profit=buyerorder_tb.objects.filter(sellerid=seller)
    return render(request,"viewcustomerorders.html",{'profit1':profit})

def orderapprove(request,id):
    profit2=buyerorder_tb.objects.filter(id=id).update(status="approved")
    return redirect("viewcustomerorders")

def orderreject(request,id):
    profit3=buyerorder_tb.objects.filter(id=id).update(status="rejected")
    return redirect("viewcustomerorders")

def trackorder(request,id):
    track=buyerorder_tb.objects.filter(id=id)
    return render(request,"trackorder.html",{'track1':track})

def trackorderAction(request):
    details=request.POST['details']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime('%H:%M')
    orderid=request.POST['id']
    track2=buyerorder_tb.objects.get(id=orderid)
    track3=trackorder_tb(detail=details,date=date,time=time,orderid=track2)
    track3.save()
    #order=buyerorder_tb.objects.filter(id=orderid)
    return redirect("viewcustomerorders")

def confirmcancel(request,id):
    conf=buyerorder_tb.objects.filter(id=id)
    conf.update(status="confirmcancel")
    quantity=conf[0].quantity
    stock=conf[0].productid.stock
    stock=int(stock)+quantity
    product=addproduct_tb.objects.filter(id=conf[0].productid.id)
    product.update(stock=stock)
    return redirect("viewcustomerorders")
    
    






















