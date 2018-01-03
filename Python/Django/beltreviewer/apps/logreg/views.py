# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *

def home_page(request):
    return render(request, "logreg/home_page.html")

def books(request):
    context = {
        'user' : User.objects.get(id  = request.session['user_id']),
        'reviews': Review.objects.all()[:3],
        'books':Book.objects.all()
    }
    return render(request, "logreg/books.html",context)

def add_page(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request,"logreg/add_page.html",context)

def book_page(request,id):
    context = {
        'book': Book.objects.get(id = id),
        'reviews': Book.objects.get(id = id).reviews.all()
    }
    return render(request, 'logreg/book_page.html', context)

def user(request, id):

    context = {
        'user' : User.objects.get(id = id),
        'totalR' : Review.objects.filter(user_id = id).count(),
        'user_reviews': Review.objects.filter(user_id = id)
    }
    return render(request, 'logreg/user.html',context)


# page-load above

def register(request):
    result = User.objects.register_validator(request.POST)
    print result
    if result[0]:
        User.objects.create(name = request.POST['name'], alias = request.POST['alias'], email = request.POST['email'],password = result[1])
        print result[1]
        messages.success(request,"registered successfully, please log in !")
        return redirect('/home')
    else:
        for key,value in result[1].iteritems():
            messages.error(request,value)
        return redirect('/home')
def signin(request):
    result = User.objects.login_validator(request.POST)
    if result[0]:
        request.session['user_id'] = result[1]
        return redirect('/books')
    else:
        for key,value in result[1].iteritems():
            messages.error(request,value)
        return redirect('/home')

def add_books(request):
    Author.objects.create(name = request.POST['author_name'])
    Book.objects.create(author = Author.objects.filter(name = request.POST['author_name'])[0],title = request.POST['title'])
    book_id = Book.objects.filter(title = request.POST['title'])[0].id
    Review.objects.create(book = Book.objects.filter(title = request.POST['title'])[0], user = User.objects.get(id = request.session['user_id']), content = request.POST['review'], rate = request.POST['rate'])
    return redirect('book_page', id = book_id)


def add_review(request):
    Review.objects.create(book = Book.objects.get(id = request.POST['book_id']), user = User.objects.get(id = request.session['user_id']), content = request.POST['review'], rate = request.POST['rate'])
    return redirect ('book_page', id  = request.POST['book_id'])

def delete(request, id,book_id):
    a = Review.objects.get(id = id )
    a.delete()
    return redirect('book_page',id = book_id)
