from typing import ContextManager
from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import OrderForm

# Create your views here.

from .models import * 






def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    # passing total customers total, order-delivered,  pending orders

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count
    pending = orders.filter(status = 'Pending').count

    # 

    context = {
        'customers' : customers, 
        'orders' : orders,
        'total_customers' :  total_customers,
        'total_orders' : total_orders,
        'delivered' : delivered,
        'pending' :  pending,
    }

    return render(request,'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request,'accounts/products.html', {'products': products}) #passing the html page and the products list

def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    orders_count = orders.count()

    context = {
        'customer' : customer,
        'orders' : orders,
        'orders_count' : orders_count,
    }
    return render(request,'accounts/customer.html',context)


def createOrder(request):

    form = OrderForm()

    if request.method == 'POST':

        #! to check the post is sending data
        # print('printing', request.POST) 

        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        

    context={'form': form}
    return render(request, 'accounts/order_form.html', context)

def updateOrder(request,pk):
    
    order = Order.objects.get(id = pk)  #*getting the instance 
    form = OrderForm(instance=order)

    if request.method == 'POST':

        #! to check the post is sending data
        # print('printing', request.POST) 

        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form' : form}
    return render(request, 'accounts/order_form.html',context)



def deleteOrder(request, pk):
    order = Order.objects.get(id = pk)  #*getting the instance 
    
    # ? why this line?  if we need the form template of the objects 
    # * but we don't need it so commenting
    #form = OrderForm(instance=order)  

    #todo (option-1) called from the delete page to delete
    if request.method == 'POST':
        order.delete()
        return redirect('/')
   
    #todo(option-2) called from the dashboard to visit delete confirmation page
    context={'item': order}  #!we are passing the item in delete.html so
    return render(request, 'accounts/delete.html', context)
