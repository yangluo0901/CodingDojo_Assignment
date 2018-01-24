# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request, "ajax_test/index.html")
def find(request):
    print request.POST['name']
    users=User.objects.filter(name__contains=request.POST['name'])
    return render(request, "ajax_test/index.html",{'users':users})
