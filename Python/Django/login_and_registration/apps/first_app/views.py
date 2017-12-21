# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages,sessions
from django.shortcuts import render,redirect
from .models import *
import bcrypt
# Create your views here.
def home_page(request):

    return render(request,'first_app/home.html')

def registration(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for key,value in errors.iteritems():
            messages.error(reqeust,value)
        return redirect('/')
    elif User.objects.filter(email = request.POST['email']).exists():
        messages.error(request,"E-mail already exists !")
        return redirect('/')
    else:
        hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'],email = request.POST['email'],password = hash_pw)
        request.session['name']  = request.POST['first_name']
        return redirect('/success')
def login(request):
    if User.objects.filter(email = request.POST['email']).exists():
        request.session['name'] = User.objects.get(email = request.POST['email']).first_name
        print User.objects.get(email = request.POST['email'])
        if  bcrypt.checkpw(request.POST['password'].encode(), User.objects.get(email = request.POST['email']).password.encode()):
            return redirect('/success')
        else:
            return redirect('/')
    else:
        messages.error(request,"E-mail does not exist")
        return redirect('/')

def success(request):

    context = {
        'name':request.session['name'],
        'users': User.objects.all()
    }
    return render(request, 'first_app/success.html', context)
