"""Module providingFunction printing python version."""

from django.shortcuts import redirect, render
from .models import Member
from .models import Order

def index(request):
    """A dummy docstring."""
    mem=Member.objects.all()
    return render(request,'index.html',{'mem':mem})
    
def orders(request):
    """A dummy docstring."""
    orders=Order.objects.all()
    return render(request,'orders.html',{'orders':orders})
    
def loginuser(request):
    """A dummy docstring."""
    return render(request,'login.html')
    
def products(request):
    """A dummy docstring."""
    return render(request,'products.html')

def single_product(request):
    """A dummy docstring."""
    return render(request,'single-product.html')

def add(request):
    """A dummy docstring."""
    return render(request,'add.html')

def addrec(request):
    """A dummy docstring."""
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['country']
    mem=Member(firstname=x,lastname=y,country=z)
    mem.save()
    return render(request,'login.html')
    
def addorder(request):
    """A dummy docstring."""
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
    """A dummy docstring."""
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
    """A dummy docstring."""
    mem=Member.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request,id):
    """A dummy docstring."""
    mem=Member.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def uprec(request,id):
    """A dummy docstring."""
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
    """A dummy docstring."""
    mem=Order.objects.get(id=id)
    mem.delete()
    return redirect("/")

def updateOrder(request,id):
    """A dummy docstring."""
    mem=Order.objects.get(id=int(id))
    return render(request,'updateOrder.html',{'order':mem})

def upOrder(request,id):
    """A dummy docstring."""
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
    """A dummy docstring."""
    x=request.POST['first']
    y=request.POST['last']
    try:
        mem=Member.objects.get(firstname=x)
        #mem=Member.objects.all()
        return render(request,'productsLoggedIn.html',{'mem':mem})
    except:
        return render(request, 'error.html')

def single_productLoggedIn(request,id):
    """A dummy docstring."""
    try:
        #mem=Member.objects.all()
        return render(request,'single-productLoggedIn.html',{'id':id})
    except:
        return render(request, 'error.html')

def myOrders(request,id):
    """A dummy docstring."""
    orders=Order.objects.filter(orderid=id)
    try:
        orders=Order.objects.filter(orderid=id)
        #mem=Member.objects.all()
        return render(request,'orders.html',{'orders':orders})
    except:
        return render(request, 'error.html')

def myOrdersOld(request,oldid,id):
    """A dummy docstring."""
    try:
        orders=Order.objects.filter(orderid=id)
        #mem=Member.objects.all()
        return render(request,'orders.html',{'orders':orders})
    except:
        return render(request, 'error.html')
