# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def purchase(request):# home page
    try:
        request.session['client']
    except:
        request.session['client'] = []
    return render(request, 'first_app/purchase.html')

def checkout(request):# direct to checkout page
    return render(request,'first_app/checkout.html')

def process(request):# handle purchase process

    if request.method == "POST":  # determine price
        if request.POST['product_id'] == "001":
            price = 19.99
        elif request.POST['product_id'] == "002":
            price = 29.99
        elif request.POST['product_id'] =="003":
            price = 4.99
        else:
            price = 49.99
        new_dict = {}
        new_dict['product_id'] = request.POST['product_id']
        new_dict['quantity'] = request.POST['quantity']
        
        new_dict['price'] = price
        request.session['bill']= price * int(request.POST['quantity']) # bill this time
        new_dict['bill'] = request.session['bill']
        request.session['client'].append(new_dict)
        try:
            request.session['total_bill']
        except:
            request.session['total_bill'] = 0
        request.session['total_bill'] += new_dict['bill']
        try:
            request.session['total_quantity']
        except:
            request.session['total_quantity'] = 0
        request.session['total_quantity'] += int(request.POST['quantity'])
        print request.session['client']
        return redirect('/amadon/checkout')

def clear(request):
    del request.session['client']
    del request.session['total_quantity']
    del request.session['total_bill']
    return redirect('/amadon')
