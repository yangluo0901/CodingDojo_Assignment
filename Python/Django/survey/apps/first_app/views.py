# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    try:
        request.session['times']
    except:
        request.session['times'] = 0
    return render(request, 'first_app/index.html')
def process(request):
    print "i am here"
    if request.method == "POST":
        request.session['times'] += 1
        name = request.POST['name']
        location = request.POST['location']
        language =  request.POST['language']
        comment = request.POST['comment']
    return redirect('/')

def result(request):
    context = {
        'name':name,
        'location':location,
        'language': lanuage,
        'comment':comment
    }
    return render(request,'first_app/result.html', context)
