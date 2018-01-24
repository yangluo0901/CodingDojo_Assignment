# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.shortcuts import render,redirect,HttpResponse
import views
import json

# Create your views here.
def index(request):
    return render(request, "ajax_test/index.html")
def find(request):

    users=User.objects.filter(name__contains=request.POST['name'])
    print users[0].name
    #return render(request, "ajax_test/index.html",context)
    return HttpResponse(json.dumps({'name':users[0].name}), content_type="application/json")
