"""onlineshopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from siteadmin import views as adminview
from seller import views as sellerview
from buyer import views as buyerview
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',adminview.index,name="index"),
    path('buyerregistration/',buyerview.buyerregistration,name="buyerregistration"),
    path('registerAction/',buyerview.registerAction,name="registerAction"),
    path('sellerregistration/',sellerview.sellerregistration,name="sellerregistration"),
    path('sellerregisterAction/',sellerview.sellerregisterAction,name="sellerregisterAction"),
    path('login/',adminview.login,name="login"),
    path('loginAction/',adminview.loginAction,name="loginAction"),
    path('viewregisteredsellers/',adminview.viewregisteredsellers,name="viewregisteredsellers"),
    path('approve<int:id>/',adminview.approve,name="approve"),
    path('reject<int:id>/',adminview.reject,name="reject"),
    path('checkusername/',adminview.checkusername,name="checkusername"),
    path('addcategory/',adminview.addcategory,name="addcategory"),
    path('addcategoryAction/',adminview.addcategoryAction,name="addcategoryAction"),
    path('updatebuyerprofile/',buyerview.updatebuyerprofile,name="updatebuyerprofile"),
    path('updatesellerprofile/',sellerview.updatesellerprofile,name="updatesellerprofile"),
    path('updateAction/',buyerview.updateAction,name="updateAction"),
    path('updatesellerAction/',sellerview.updatesellerAction,name="updatesellerAction"),
    path('addproduct/',sellerview.addproduct,name="addproduct"),
    path('addproductAction/',sellerview.addproductAction,name="addproductAction"),
    path('viewaddproduct/',sellerview.viewaddproduct,name="viewaddproduct"),
    path('delete<int:id>/',sellerview.delete,name="delete"),
    path('edit<int:id>/',sellerview.edit,name="edit"),
    path('editupdateAction/',sellerview.editupdateAction,name="editupdateAction"),
    path('viewselleraddedproducts/',buyerview.viewselleraddedproducts,name="viewselleraddedproducts"),
    path('addtocart<int:productid>/',buyerview.addtocart,name="addtocart"),
    path('buynowAction/',buyerview.buynowAction,name="buynowAction"),
    path('viewcart/',buyerview.viewcart,name="viewcart"),
    path('cartdelete<int:id>/',buyerview.cartdelete,name="cartdelete"),
    path('placetheorderAction/',buyerview.placetheorderAction,name="placetheorderAction"),
    path('myorders/',buyerview.myorders,name="myorders"),
    path('cancel<int:id>/',buyerview.cancel,name="cancel"),
    path('viewcustomerorders/',sellerview.viewcustomerorders,name="viewcustomerorders"),
    path('orderapprove<int:id>/',sellerview.orderapprove,name="orderapprove"),
    path('orderreject<int:id>/',sellerview.orderreject,name="orderreject"),
    path('trackorder<int:id>/',sellerview.trackorder,name="trackorder"),
    path('trackorderAction/',sellerview.trackorderAction,name="trackorderAction"),
    path('trackmyorder<int:id>/',buyerview.trackmyorder,name="trackmyorder"),
    path('confirmcancel<int:id>/',sellerview.confirmcancel,name="confirmcancel"),
    path('searchproduct/',buyerview.searchproduct,name="searchproduct"),
    path('productsearchAction/',buyerview.productsearchAction,name="productsearchAction"),
    path('searchcategory/',buyerview.searchcategory,name="searchcategory"),
    path('searchcategoryAction/',buyerview.searchcategoryAction,name="searchcategoryAction"),
    path('forgotpassword/',adminview.forgotpassword,name="forgotpassword"),
    path('forgotpasswordAction/',adminview.forgotpasswordAction,name="forgotpasswordAction"),
    path('createnewpasswordAction/',adminview.createnewpasswordAction,name="createnewpasswordAction"),
    path('enternewpasswordAction/',adminview.enternewpasswordAction,name="enternewpasswordAction"),
    path('logout/',adminview.logout,name="logout")
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
