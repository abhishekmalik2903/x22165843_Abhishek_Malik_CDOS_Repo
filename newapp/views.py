from django.shortcuts import redirect, render
from flask import session, url_for
from .models import Member
from .models import Order

def index(request):
    mem=Member.objects.all()
    return render(request,'index.html',{'mem':mem})
    
def orders(request):
    orders=Order.objects.all()
    return render(request,'orders.html',{'orders':orders})
    
def loginuser(request):
    return render(request,'login.html')
    
def products(request):
    return render(request,'products.html')

def single_product(request):
    return render(request,'single-product.html')

def add(request):
    return render(request,'add.html')

def addrec(request):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['country']
    mem=Member(firstname=x,lastname=y,country=z)
    mem.save()
    return render(request,'login.html')
    
def addorder(request):
    a=request.POST['first']
    b=request.POST['last']
    c=request.POST['address']
    d=request.POST['city']
    e=request.POST['state']
    f=request.POST['zip']
    g=request.POST['country']
    order=Order(firstname=a,lastname=b,address=c,city=d,state=e,zipcode=f,country=g)
    order.save()
    return redirect("/")

def addorderLoggedIn(request):
    a=request.POST['first']
    b=request.POST['last']
    c=request.POST['address']
    d=request.POST['city']
    e=request.POST['state']
    f=request.POST['zip']
    g=request.POST['country']
    h=request.POST['orderid']
    order=Order(firstname=a,lastname=b,address=c,city=d,state=e,zipcode=f,country=g,orderid=h)
    order.save()
    testurl = 'myOrders/' + h
    return redirect(testurl)

def delete(request,id):
    mem=Member.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request,id):
    mem=Member.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def uprec(request,id):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['country']
    mem=Member.objects.get(id=id)
    mem.firstname=x
    mem.lastname=y
    mem.country=z
    mem.save()
    return redirect("/")
    
def deleteOrder(request,id):
    mem=Order.objects.get(id=id)
    mem.delete()
    return redirect("/")

def updateOrder(request,id):
    mem=Order.objects.get(id=int(id))
    return render(request,'updateOrder.html',{'order':mem})

def upOrder(request,id):
    a=request.POST['first']
    b=request.POST['last']
    c=request.POST['address']
    d=request.POST['city']
    e=request.POST['state']
    f=request.POST['zip']
    g=request.POST['country']
    mem=Order.objects.get(id=id)
    mem.firstname=a
    mem.lastname=b
    mem.address=c
    mem.city=d
    mem.state=e
    mem.zipcode=f
    mem.country=g
    mem.save()
    testurl = 'myOrders/' + mem.orderid
    return redirect(testurl)
    
def login(request):
    x=request.POST['first']
    y=request.POST['last']
    try:
        mem=Member.objects.get(firstname=x)
        #mem=Member.objects.all()
        return render(request,'productsLoggedIn.html',{'mem':mem})
    except:
        return render(request, 'error.html')

def single_productLoggedIn(request,id):
    try:
        #mem=Member.objects.all()
        return render(request,'single-productLoggedIn.html',{'id':id})
    except:
        return render(request, 'error.html')

def myOrders(request,id):
    orders=Order.objects.filter(orderid=id)
    try:
        orders=Order.objects.filter(orderid=id)
        #mem=Member.objects.all()
        return render(request,'orders.html',{'orders':orders})
    except:
        return render(request, 'error.html')

def myOrdersOld(request,oldid,id):
    try:
        orders=Order.objects.filter(orderid=id)
        #mem=Member.objects.all()
        return render(request,'orders.html',{'orders':orders})
    except:
        return render(request, 'error.html')
