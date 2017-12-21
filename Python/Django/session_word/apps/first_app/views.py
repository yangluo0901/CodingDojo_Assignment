# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from datetime import datetime
# Create your views here.
def index(request):
    try:
        request.session['new_word']
    except:
        request.session['new_word'] = []
    return render(request,'first_app/index.html')

def process(request):

    new_word = request.session['new_word']
    new_dict = {}
    new_dict['word'] = request.POST['word']
    new_dict['color'] = request.POST['color']
    new_dict['font'] = request.POST['font']
    new_dict['add_time'] = datetime.now().strftime("%H:%M %p, %B %d, %Y")
    new_word.append(new_dict)
    request.session['new_word'] = new_word
    print request.session['new_word']
    return redirect('/session_word')

def clear(request):
    del request.session['new_word']
    return redirect('/session_word')
