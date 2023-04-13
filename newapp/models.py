from django.db import models

class Member(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    
class Order(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    orderid=models.CharField(max_length=100)