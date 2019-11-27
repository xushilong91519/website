from django.shortcuts import render
from django.http import HttpResponse
from web1.models import Order,Container
from django.template.loader import get_template
from django.utils import timezone
import re

# Create your views here.

def manage_order(request):
    orders=Order.objects.all()
    return render(request,'web1/index.html',locals())

def order_detail(request,order_number):
    order=Order.objects.get(order_number=order_number)
    containers=order.container_set.all()
    return render(request,'web1/order.html',locals())

def add_order(request):
    new_order_number=''.join(re.split('[\s\-\+\.:]',str(timezone.now()))[0:7])
    return render(request,'web1/new_order.html',locals())

def submit_order(request,order_number):
    new_order=Order()
    new_order.order_number=order_number
    new_order.customer_code=request.POST['customer_code']
    new_order.order_date=request.POST['order_date']
    new_order.assign_date=request.POST['assign_date']
    new_order.survey_locations=request.POST['survey_locations']
    new_order.depot_code=request.POST['depot_code']
    new_order.depot_name=request.POST['depot_name']
    new_order.unit_type=request.POST['unit_type']
    new_order.qty=request.POST['qty']
    new_order.release_number=request.POST['release_number']
    new_order.survey_code=request.POST['survey_code']
    new_order.remark=request.POST['remark']
    new_order.save()
    for i in range(int(request.POST['container_count'])):
        new_order.container_set.create(container_number=request.POST['container%s'%i],content=request.POST['container%s_content'%i])
    new_order.save()
    orders=Order.objects.all()
    return render(request,'web1/index.html',locals())

def edit_order(request,order_number):
    order=Order.objects.get(order_number=order_number)
    order.customer_code=request.POST['customer_code']
    order.survey_locations=request.POST['survey_locations']
    order.depot_code=request.POST['depot_code']
    order.depot_name=request.POST['depot_name']
    order.unit_type=request.POST['unit_type']
    order.release_number=request.POST['release_number']
    order.survey_code=request.POST['survey_code']
    order.remark=request.POST['remark']
    order.save()
    return render(request,'web1/order.html',locals())

def container_detail(request,container_number):
    container=Container.objects.get(container_number=container_number)
    order=container.order
    containers=order.container_set.all()
    return render(request,'web1/container.html',locals())
