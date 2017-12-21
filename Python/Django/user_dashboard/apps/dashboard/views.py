# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render,redirect
from django.contrib import messages
import bcrypt
# page-load functions:
def home(request):
    return render(request,'dashboard/home.html')

def signin_page(request):
    return render(request,'dashboard/signin.html')
def register_page(request):
    return render(request,'dashboard/register.html')
def dashboard(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'dashboard/dashboard.html',context)
def dashboard_admin(request):

    context = {
        'users': User.objects.all()
    }
    return render(request, 'dashboard/dashboard_admin.html',context)

def edit_page(request, id):
    context = {
        'user': User.objects.get(id = id)
    } # 'user' here: the user whose information will be modified
    return render(request, 'dashboard/edit_page.html',context)

def edit_self_page(request): # user can only edit theirselves
    context = {
        'user' : User.objects.get(id = request.session['user_id'])
    }
    return render(request, 'dashboard/edit_self_page.html', context)
    
# handlers:

def signin(request):
    result = User.objects.login_validator(request.POST)
    if type(result) == dict:
        for key,value in result.iteritems():
            messages.error(request,value)
        return redirect('/signin')
    else:
        request.session['user_id'] = result.id
        request.session['login_user'] = result.first_name # store login user information inside session
                                                        # so that these information can be used for rendering page
        if result.level == 9: # admin
            return redirect('/dashboard/admin')
        else:
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



def edit(request):
    a = User.objects.get(id = request.POST['target_id'])
    if request.POST.get('first_name'):
        a.first_name = request.POST.get('first_name')
    if request.POST.get('last_name'):
        a.last_name = request.POST.get('last_name')
    if request.POST.get('email'):
        a.email = request.POST.get('email')
    if request.POST.get('level'):
        if request.POST.get('level') == "Normal":
            a.level = 1
        else:
            a.level = 9
    try:
        if request.POST['password'] and request.POST['con_pw']:
            if request.POST['password'] == request.POST['con_pw']:
                a.password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt(15))
            else:
                messages.error(request,"Password do no match, try it again")
                return redirect('eidt', id = request.POST.get('target_id'))

        else:
            messages.error(request,"Please type in password")
            return redirect('edit', id = request.POST.get('target_id'))
            print " i am here"
    except:
        pass
    a.save()
    return redirect('/dashboard/admin')

def remove(request,id):
    a = User.objects.get(id = id)
    a.delete()
    if len(User.objects.all()) == 0:
        return redirect('/signin') # return back to sign in page, when all records are deleted
    return redirect('/dashboard/admin')
