# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
def index(request):
    response = "Hello, I am your first reqeust!"
    return HttpResponse(response)
