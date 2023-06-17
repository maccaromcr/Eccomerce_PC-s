from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#Creacion modelo cliente
class costumer(models.Model):
    User = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Creacion modelo producto
class product(models.Model):
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False , null=True, blank=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name  

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''

        return url


class order(models.Model):
    costumer = models.ForeignKey(costumer, on_delete=models.SET_NULL, blank=True, null=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_car_total(self):
        orderitems = self.orderItem.all()
        total = sum([items.get_total for items in orderitems])
        return total
        

    
    
    @property
    def get_car_item(self):
        orderitems = self.orderItem_set.all()
        total = sum([item.quantity  for item in orderitems])
        return total    
    

    

class orderItem(models.Model):
    products = models.ForeignKey(product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(order, on_delete=models.SET_NULL, blank=True, null=True, related_name='orderItems' )
    quantity =models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


    @property
    def get_total(self):
        total = self.products.price*self.quantity
        return total


class ShippingAddress(models.Model):
    costumer = models.ForeignKey(costumer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    zipcode = models.CharField(max_length=200,null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address