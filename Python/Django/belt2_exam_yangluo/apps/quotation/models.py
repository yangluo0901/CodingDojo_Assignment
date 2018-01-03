# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
import re
import bcrypt
# Create your models here.


email_regex = re.compile(r'[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        print datetime.datetime.now()
        if len(postData['name']) < 3:
            errors['name_length'] = "Name should be more than 3"
        if not email_regex.match(postData['email']):
            errors['email'] = "Invalid e-mail address"
        if self.filter(email = postData['email']):
            errors['email'] = 'Email already exists !'
        if len(postData['password']) < 8:
            errors['password'] = "Invalid passwpord"
        if postData['password'] != postData['con_password']:
            errors['match'] = "Password does not match"
        # if postData['birthdate'] > datetime.datetime.now():
        #     errors['birthdate'] = 'Birth day can not be future !'
        if errors:
            return False, errors
        else:
            hash_pw =  bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt(15))
            return True, hash_pw

    def login_validator(self, postData):
        errors = {}
        print postData['email']
        print len(self.filter(email = postData['email']))
        if len(self.filter(email = postData['email'])) == 0:
            errors['email'] = 'Email does not exists !'
        else:
            password = self.filter(email = postData['email'])[0].password
            if not bcrypt.checkpw(postData['password'].encode(), password.encode()):
                errors['password'] = 'wrong password !'
        if errors:
            return False,errors
        else:
            login_id = self.filter(email = postData['email'])[0].id
            return True, login_id

class QuoteManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        if len(postData['quoted_by']) < 3 :
            errors['quoted_by'] = "Name should be more than 3"
        if len(postData['quote']) <10 :
            errors['quote'] = "Message should be at least 10 characters"
        if errors:
            return False, errors
        else:
            return True, postData['quote']

class User(models.Model):
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    birthdate = models.CharField(max_length =20)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()



class Quote(models.Model):
    content = models.TextField()
    quoted_by = models.CharField(max_length = 100, null = True)
    user = models.ForeignKey(User, related_name = 'quotes')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    favorites = models.ManyToManyField(User, related_name = 'favorite_quotes',)
    objects = QuoteManager()
