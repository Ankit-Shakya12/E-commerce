from django.db import models
import datetime

# Category 
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Customer
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Product  
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0,decimal_places=2,max_digits=10)
    description = models.CharField(max_length=300,default='',blank=True, null=True)
    image = models.ImageField(upload_to='product/')
    category = models.ForeignKey(Category,default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
# Customer Order 
class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product
