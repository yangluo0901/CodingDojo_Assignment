# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
    return render(request,'quotation/index.html')

def all_quotes(request):
    list = []
    quotes = Quote.objects.all()
    for quote in quotes:
        list.append(quote)
        for element in quote.favorites.all():
            if  element.id == request.session['login_id'] :
                list.pop()
    context = {
        'list':list,
        'quotes':quotes,
        'user': User.objects.get(id = request.session['login_id'])
    }
    return render(request, 'quotation/all_quotes.html',context)



# page load functions above
def register(request):
    result = User.objects.register_validator(request.POST)
    if result[0] == False:
        for key,value in result[1].iteritems():
            messages.error(request,value)
        return redirect('/main')
    else:
        hash_pw = result[1]
        User.objects.create(name = request.POST['name'],email = request.POST['email'],password = hash_pw, birthdate = request.POST['birthdate'])
        messages.success(request, "Registered successfully !")
        return redirect('/main')

def login(request):
    result = User.objects.login_validator(request.POST)
    if result[0] == False:
        for key,value in result[1].iteritems():
            messages.error(request,value)
        return redirect('/main')
    else:
        request.session['login_id'] = result[1]
        return redirect('/quotes')


def add_quote(request):
    result = Quote.objects.basic_validator(request.POST)
    if result[0] == False:
        print " i am here"
        for key,value in result[1].iteritems():
            print value
            messages.error(request, value)
        return redirect('/quotes')
    else:
        Quote.objects.create(user = User.objects.get(id = request.session['login_id']), content = result[1],quoted_by = request.POST['quoted_by'])
        return redirect('/quotes')


def add_favorite(request):
    quote = Quote.objects.get(id = request.POST.get('quote_id'))
    favorite_user = User.objects.get(id  = request.session['login_id'])
    quote.favorites.add(favorite_user)
    return redirect('/quotes')

def remove_favorite(request):
    quote = Quote.objects.get(id = request.POST.get('quote_id'))
    favorite_user = User.objects.get(id  = request.session['login_id'])
    quote.favorites.remove(favorite_user)
    return redirect('/quotes')

def individual(request,id):
    context = {
        'user':User.objects.get(id = id),
        'quotes': User.objects.get(id = id).quotes.all()

    }
    return render(request, 'quotation/individual.html', context)
