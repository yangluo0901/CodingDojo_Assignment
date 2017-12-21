# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render,redirect,HttpResponse
from .models import *
import datetime
def index(request):
    context = {
        'users' : User.objects.all()
    }
    return render(request,'crud/index.html',context)

def show(request, id):
    context ={
        'user' : User.objects.get(id = id)
    }

    return render(request,'crud/show.html',context)
def edit(request, id):
    context = {
        'user' : User.objects.get(id = id)
    }

    return render(request,'crud/edit.html', context)

def update(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for key,error in errors.iteritems():
            messages.error(request,error,extra_tags = key)
        return redirect('/users/update')
    else:
        user_id = int(request.POST['user_id'])
        a = User.objects.get(id = user_id )
        a.first_name = request.POST['first_name']
        a.last_name = request.POST['last_name']
        a.email = request.POST['email']
        a.update_at = datetime.datetime.now().strftime('')
        a.save()
        return redirect('/users')
def new(request):
    return render(request,'crud/new.html')

def create(request):
    errors = User.objects.basic_validator(request.POST)

    if len(errors):
        for key,error in errors.iteritems():
            messages.error(request,error,extra_tags = key)
        print  messages
        print " i am here"
        return redirect('/users/new')
    else:
        User.objects.create(first_name=request.POST['first_name'], last_name =request.POST['last_name'], email = request.POST['email'])
        return redirect('/users')

def destroy(request, id):
    u = User.objects.get(id = id)
    u.delete()
    return redirect('/users')
