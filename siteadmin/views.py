from django.shortcuts import render,redirect
from siteadmin.models import *
from buyer.models import *
from seller.models import *
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def loginAction(request):
    username=request.POST['username']
    password=request.POST['password']
    admin=adminlogin_tb.objects.filter(username=username,password=password)
    buyer=buyerregistration_tb.objects.filter(username=username,password=password)
    seller=sellerregistration_tb.objects.filter(username=username,password=password)
    if admin.count()>0:
        request.session['adminid']=admin[0].id
        return render(request,"adminhome.html")
    elif buyer.count()>0:
        request.session['buyerid']=buyer[0].id
        return render(request,"buyerhome.html")
    elif seller.count()>0:
        status=seller[0].status
        if status=="approved":
            request.session['sellerid']=seller[0].id
            return render(request,"sellerhome.html")
        else:
            messages.add_message(request,messages.INFO,"waiting for approval")
            return redirect("login")
    else:
        messages.add_message(request,messages.INFO,"login failed")
        return render(request,"login.html")

def viewregisteredsellers(request):
    admin=request.session['adminid']
    seller=sellerregistration_tb.objects.all()
    return render(request,"viewregisteredsellers.html",{'seller':seller})

def approve(request,id):
    seller=sellerregistration_tb.objects.filter(id=id).update(status="approved")
    return redirect("viewregisteredsellers")

def reject(request,id):
    seller=sellerregistration_tb.objects.filter(id=id).update(status="rejected")
    return redirect("viewregisteredsellers")

def checkusername(request):
    username=request.GET['username']
    admin=adminlogin_tb.objects.filter(username=username)
    buyer=buyerregistration_tb.objects.filter(username=username)
    seller=sellerregistration_tb.objects.filter(username=username)
    if len(admin)>0:
        msg="exist"
    elif len(seller)>0:
        msg="exist"
    elif len(buyer)>0:
        msg="exist"
    else:
        msg="not exist"
    return JsonResponse({'valid':msg})

def addcategory(request):
    return render(request,"addcategory.html")

def addcategoryAction(request):
    name=request.POST['name']
    category=addcategory_tb(name=name)
    category.save()
    return redirect('addcategory')

def forgotpassword(request):
    return render(request,"forgotpassword.html")

def forgotpasswordAction(request):
    username=request.POST['username']
    buyer1=buyerregistration_tb.objects.filter(username=username)
    seller1=sellerregistration_tb.objects.filter(username=username)
    if buyer1.count()>0:
        return render(request,"createnewpassword.html",{'data':username})
    elif seller1.count()>0:
        return render(request,"createnewpassword.html",{'data':username})
    else:
        messages.add_message(request,messages.INFO,"wrong password")
        return render(request,"login.html")

def createnewpasswordAction(request):
    name=request.POST['name']
    dob=request.POST['dob']
    country=request.POST['country']
    username=request.POST['username']
    buyer2=buyerregistration_tb.objects.filter(name=name,dob=dob,country=country,username=username)
    seller2=sellerregistration_tb.objects.filter(name=name,dob=dob,country=country,username=username)
    if buyer2.count()>0:
        return render(request,"enternewpassword.html",{'data':username})
    elif seller2.count()>0:
        return render(request,"enternewpassword.html",{'data':username})
    else:
        messages.add_message(request,messages.INFO,"wrong data")
        return render(request,"login.html")

def enternewpasswordAction(request):
    username=request.POST['username']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']
    if newpassword == confirmpassword:
        buyer3=buyerregistration_tb.objects.filter(username=username)
        seller3=sellerregistration_tb.objects.filter(username=username)
        if seller3.count()>0:
            request.session['sellerid']=seller3[0].id
            seller3=request.session['sellerid']
            seller3=sellerregistration_tb.objects.filter(id=seller3).update(password=newpassword)
        elif buyer3.count()>0:
            request.session['buyerid']=buyer3[0].id
            buyer3=request.session['buyerid']
            buyer3=buyerregistration_tb.objects.filter(id=buyer3).update(password=newpassword)
            messages.add_message(request,messages.INFO,"password changed successfully")
            request.session.flush()
            return render(request,"login.html")          
    else:
        messages.add_message(request,messages.INFO,"attempt failed")
    return render(request,"enternewpassword.html",{'data':username})

def logout(request):
    request.session.flush()
    return render(request,"index.html")
        
    
    

    





























