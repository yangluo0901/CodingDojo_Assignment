# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse, redirect

# Create your views here.
def register(request):
    response = "placeholder for users to create a new user record"
    return HttpResponse(response)
def login(request):
    response = "placeholder for users to login"
    return HttpResponse(response)
def new(request):
    response = " I can not understand the description"
    return HttpResponse(response)
def users(request):
    response = "placeholder to later display all the list of users"
    return HttpResponse(response)
