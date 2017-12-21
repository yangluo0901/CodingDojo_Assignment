# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def register_validator(self,postData):
        email_regex = re.compile(r'[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

        errors = {}
        if not email_regex.match(postData['email']):
            errors['email'] = "Invalid email address !"
        elif len(self.filter(email=postData['email'])) > 0:
            errors['email'] = "E-mail already exists !"
        if len(postData['password']) < 7:
            errors['password'] = "Password should not be less than 7 characters !"
        if not errors:
            hashed = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt(15))
            new_user = self.create(
                first_name=postData['first_name'],
                last_name=postData['last_name'],
                email=postData['email'],
                password=hashed,
                level = "1"
            )
            return new_user
        return errors
    def login_validator(self,postData):
        errors = {}
        if len(self.all()) > 0:
            if len(self.filter(email = postData['email'])) != 0:
                user = self.get(email = postData['email'])
                if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                    errors['password'] = "Password does not match E-mail !"
            else:
                errors['email'] = "E-mail does not exist !"


        else:
            errors['empty'] = "You are first user, please register"
        if not errors:
            user = self.filter(email = postData['email'])[0]
            return user
        return errors
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    level = models.IntegerField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()


class Post(models.Model):
    content = models.TextField()
    recipient_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User,related_name = 'posts')

class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User,related_name = 'messages')
    post = models.ForeignKey(Post, related_name = 'messages')
