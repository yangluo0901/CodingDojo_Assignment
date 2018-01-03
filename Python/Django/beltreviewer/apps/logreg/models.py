# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.db import models
import bcrypt

email_regex = re.compile(r'[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
class UserManager(models.Manager):

    def register_validator(self,postData):
        errors = {}

        if len(postData['name']) < 5 :
            errors['name'] = "Name should be at least 5 characters !"
        if len(postData['password']) < 8 :
            errors['password'] = "Password should be at least 5 characters !"
        elif postData['password'] != postData['confirm_pw']:
                errors['passowrd'] = " Password does not match !"
        if not email_regex.match(postData['email']):
            errors['email'] = "Invaid E-mail !"
        elif  len(User.objects.filter(email = postData['email'])) != 0:
            errors['email'] = "Email already exists !"
        if errors:
            return False,errors
        else:
            password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt(15))
            return True,password
    def login_validator(self,postData):
        errors = {}

        if postData['email']:

             if User.objects.filter(email = postData['email'])[0] == 0 :
                 errors['email'] = " E-mail does not exist !"
             else:
                user_id = User.objects.get(email = postData['email']).id
                password = User.objects.get(id = user_id).password
                print password +"store"
                if postData['password']:

                    if not bcrypt.checkpw(postData['password'].encode(), password.encode()):
                        print "i m HERE"
                        errors['password'] = 'Wrong Password !'
                else:
                    errors['password'] = " Password needed to login !"
        else:
            errors['email'] = "Please input your E-mail !"
        if errors:
             return False,errors
        else:
            return True,user_id



class User(models.Model):
    name = models.CharField(max_length = 255)
    alias = models.CharField(max_length = 255)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Author(models.Model):
    name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Book(models.Model):
    title = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(Author, related_name = 'books')




class Review(models.Model):
    content = models.TextField()
    rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, related_name = 'reviews')
    book = models.ForeignKey(Book, related_name = 'reviews')
