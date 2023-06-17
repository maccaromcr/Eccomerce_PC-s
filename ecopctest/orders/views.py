from django.shortcuts import render
from django.http import JsonResponse
from .models import * 
import json 


# Create your views here.

def store(request):
    
    if request.user.is_authenticated:
        costumer = request.user.costumer
        orders, created = order.objects.get_or_create(costumer=costumer, complete=False)
        items = orders.orderItems.all()
        carItems = order.get_car_item
       
    else:
        items = []
        orders = {'get_car_total':0 , 'get_car_item':0}
        carItems = order['get_car_item']  
    
    
    products = product.objects.all()
    context = {'product':products, 'carItems:':carItems}
    return render(request,'store/store.html',context)

def car(request):

    if request.user.is_authenticated:
        costumer = request.user.costumer
        orders, created = order.objects.get_or_create(costumer=costumer, complete=False)
        items = orders.orderItems.all()
        carItems = order.get_car_item
       
    else:
        items = []
        orders = {'get_car_total':0 , 'get_car_item':0}
        carItems = order['get_car_item'] 


        #context = {}
    context = {'Items':items,'orders':order, 'carItems':carItems }
    return render(request,'store/car.html',context)

def checkout(request):

    if request.user.is_authenticated:
        costumer = request.user.costumer
        orders, created = order.objects.get_or_create(costumer=costumer, complete=False)
        items = orders.orderItems.all()
        carItems = order.get_car_item
       
    else:
        items = []
        orders = {'get_car_total':0 , 'get_car_item':0}
        carItems = order['get_car_item'] 


    #context = {}
    context = {'Items':items,'orders':order, 'carItems':carItems }
    return render(request,'store/checkout.html',context)



def updateItem(request):
    data = json.loads(request.data)
    productId = data['productId']
    action = data['action']
    
    
    print('Action:', action)
    print('productId:', productId)
    
    costumer = request.user,costumer
    product = product.objects.get(id=productId)
    orders, created = order.objects.get_or_create(costumer=costumer, complete=False)
    
    orderItem, created = orderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
        
        
    orderItem.save() 
    
    if orderItem.quantity <= 0:
        orderItem.delete()   


            
    return JsonResponse('Item agregado correctamente', safe=False)