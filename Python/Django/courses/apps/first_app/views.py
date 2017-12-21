# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect,HttpResponse
from .models import *
from django.contrib import messages
from datetime import datetime
# Create your views here.
def home(request):
    context = {
        'course':Course.objects.all()
    }
    return render( request,'first_app/home.html',context)


def add(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for key,value in errors.iteritems():
            messages.error(request,value)
        return redirect('/')
    else:
        Course.objects.create(name = request.POST['name'], desc = request.POST['desc'], created_at = datetime.now())
        return redirect('/')

def destroy_page(request,id):
    context = {
        'course': Course.objects.get(id = id)
    }
    return render(request,'first_app/destroy.html',context)

def destroy(request,id):
    a = Course.objects.get(id = id )
    a.delete()
    print Course.objects.all().values()
    return redirect('/')
