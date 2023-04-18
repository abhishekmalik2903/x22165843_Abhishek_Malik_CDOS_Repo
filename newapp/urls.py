from django.urls import path
from . import views

urlpatterns = [
    path('',views.products,name="products"),
    path('add/',views.add,name="add"),
    path("addrec/",views.addrec,name="addrec"),
    path("addorder/",views.addorder,name="addorder"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    path('addorderLoggedIn/myOrders/deleteOrder/<str:id>/',views.deleteOrder,name="deleteOrder"),
    path('addorderLoggedIn/myOrders/updateOrder/<int:id>/',views.updateOrder,name="updateOrder"),
    path('update/uprec/<int:id>/',views.uprec,name="uprec"),
    path('updateOrder/upOrder/<str:id>/',views.upOrder,name="upOrder"),
    path('updateOrder/upOrder/<str:oldid>/myOrders/<str:id>',views.myOrdersOld,name="myOrdersOld"),
    path('loginuser/',views.loginuser,name="loginuser"),
    path('login/',views.login,name="login"),
    path('login/login',views.login,name="login"),
    path('index/',views.index,name="index"),
    path('orders/',views.orders,name="orders"),
    path('single_product/',views.single_product,name="single_product"),
    path('single_product/single_product',views.single_product,name="single_product"),
    path('addorderLoggedIn/',views.addorderLoggedIn,name="addorderLoggedIn"),
    path('login/single_product/<str:id>',views.single_productLoggedIn,name="single_productLoggedIn"),
    path('myOrders/<str:id>',views.myOrders,name="myOrders"),
    path('addorderLoggedIn/myOrders/<str:id>',views.myOrders,name="myOrders"),
    path('/myOrders/deleteOrder/<str:id>',views.deleteOrder,name="deleteMyOrders")
]