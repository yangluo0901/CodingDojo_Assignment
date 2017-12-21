# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,HttpResponse
from django.utils.crypto import get_random_string
# Create your views here.
def index(request):
    try:
        request.session['attempt']
    except:
        request.session['attempt'] = 0
    return render(request,'first_app/index.html')

def generate(request):
    request.session['attempt'] += 1
    request.session['string'] = get_random_string(length=14)
    return redirect('/')

def reset(request):

    del request.session['attempt']
    del request.session['string']
    return redirect('/')
