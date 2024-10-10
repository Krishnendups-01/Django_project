from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class product(models.Model):
#     category1 = models.CharField(max_length=200)
#     name = models.CharField(max_length=200)
#     rate = models.IntegerField()
#     images = models.FileField(upload_to='products/images', max_length=100)
#     description = models.TextField()
#     def __str__(self):
#         return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    images = models.FileField(upload_to= 'cat')
    def __str__(self):
        return self.name
    
class product(models.Model):
    category = models.ForeignKey(Category,on_delete= models.CASCADE)
    name = models.CharField(max_length=200)
    rate = models.IntegerField()
    images = models.FileField(upload_to='products/images', max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)   
    Product=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    def __str__(self):
        return self.Product.name
    # def item_price(self):
    #      return self.quantity * self.Product.rate
    
#     def get_total_price(self):
#         return sum(item.get_total_item_price() for item in self.CartItem_set.all)

# class CartItem(models.Model):
#     Product=models.ForeignKey(product,on_delete=models.CASCADE)
#     cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
#     quantity=models.PositiveIntegerField(default=1)
#     def __str__(self):
#         return f"{self.quantity}x{self.Product.name}"
#     def get_total_item_price(self):
#         return self.quantity * self.Product.rate

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=200)
    def __str__(self):
        return self.address
