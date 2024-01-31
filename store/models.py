from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=20)
    image = image = models.ImageField(upload_to='uploads/product/', blank=True, null=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    #password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=99.99)
    dimension = models.IntegerField(default=1)
    cantRoom = models.IntegerField(default=1)
    cantFloor = models.IntegerField(default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    width = models.FloatField(default=1)
    cantBathroom = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Face(models.Model):
    name = models.CharField(max_length=100, default='a', blank=True)
    image = models.ImageField(upload_to='uploads/product/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    

class Order(models.Model):
    date = models.DateField(default=datetime.datetime.today)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    face= models.ForeignKey(Face, on_delete=models.CASCADE, default=1, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    adress = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=25, default='', blank=True)
    status =models.BooleanField(default=False)

    def __str__(self):
        return f'{self.customer} {self.product}'
    
class Architect(models.Model):
    name = models.CharField(max_length=50)
    qualification = models.CharField(max_length=100, blank=True, null=True)
    positions = models.CharField(max_length=100, blank=True, null=True)
    experience = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/product/', blank=True, null=True)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'
