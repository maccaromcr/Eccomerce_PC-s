from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(costumer)
admin.site.register(product)
admin.site.register(order)
admin.site.register(orderItem)
admin.site.register(ShippingAddress)

