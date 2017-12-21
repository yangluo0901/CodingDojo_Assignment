# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from random import *
from datetime import datetime
from django.shortcuts import render, redirect

def index(request):

    return render(request,'first_app/index.html')

def process(request):
    new_dict = {}
    new_dict['time'] = datetime.now().strftime('%Y/%m/%d  %H:%M %p')
    new_dict['location'] = request.POST['location']
    temp_location = request.POST['location']
    if temp_location == "house":
        new_dict['gold'] = randint(2,5)
    elif temp_location == "farm":
        new_dict['gold'] = randint(10,20)
    elif temp_location == "cave":
        new_dict['gold'] = randint(5,10)
    elif temp_location == "casino":
        if randint(0,1) == 0:
            new_dict['gold'] = randint(0,50)
        else:
            new_dict['gold'] = randint(0,50) * -1
    try:
        request.session['ninja_money']
    except:
        request.session['ninja_money'] = []
    temp =  request.session['ninja_money']
    temp.append(new_dict)
    request.session['ninja_money'] = temp
    # dont understand why in this way, but it really works
    print request.session['ninja_money']
    return redirect('/')
