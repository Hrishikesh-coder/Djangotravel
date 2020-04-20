from django.db import models


class Destination(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc =  models.TextField()
    price =  models.IntegerField() 
    

class Reviews(models.Model):
    name = models.CharField(max_length=100)
    destination = models.CharField(max_length=200,default='Hrishikesh')
    review = models.TextField()
    heading = models.CharField(max_length=20)

class Cart(models.Model):
    username = models.CharField(max_length=200)
    cart = models.IntegerField(default=0)
    destination = models.CharField(max_length=200,default='Kolkata')
    quantity = models.IntegerField(default=1)


    
