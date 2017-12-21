# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'dashboard/home.html')

def signin_page(request):
    return render(request,'dashboard/signin.html')
def register_page(request):
    return render(request,'dashboard/register.html')

def signin(request):
    result = User.objects.login_validator(request.POST)
    if type(result) == dict:
        for key,value in result.iteritems():
            messages.error(request,value)
        return redirect('/signin')
    else:
        request.session['user_id'] = result.id
        request.session['login_user'] = result.first_name
    return redirect('/dashboard')

def register(request):
    result = User.objects.register_validator(request.POST)
    if type(result) == dict:
        for key,value in result.iteritems():
            messages.error(request,value)
        return redirect('/register')
    if len(User.objects.all()) == 1:
        result.level = 9
        result.save()

    return redirect('/signin')


def dashboard(request):

    context = {
        'users': User.objects.all()
    }
    return render(request, 'dashboard/dashboard.html',context)

def show(request, id):
    context = {
        'user' : User.objects.get(id = id),
        'posts' : Post.objects.filter(recipient_id = id).reverse()
    }
    request.session['recipient_id'] = id
    return render(request,'dashboard/show_page.html', context)


def post(request):
    Post.objects.create(user = User.objects.get(id = request.session['user_id']),content = request.POST['post'], recipient_id=request.POST.get('recipient_id'))
    return redirect('show', id = request.POST['recipient_id'])



def message(request):
    # print request.POST.get('message')
    # print  request.POST.get('post_id')
    # print " i am here"
    Message.objects.create(user = User.objects.get(id =request.session['user_id']),content = request.POST.get('message'), post = Post.objects.get(id = request.POST.get('post_id')))
    return redirect('show', id = request.session['recipient_id'])
