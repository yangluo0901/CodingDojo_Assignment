# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
# Create your models here.
email_regex = re.compile(r'[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2 or len(postData['last_name']) < 2:
            errors['name_length'] = "Name should be more than 2"
        if postData['first_name'].isalpha() == False or postData['last_name'] == False:
            errors['name_alpha'] = "Name should be composed of characters"
        if not email_regex.match(postData['email']):
            errors['email'] = "Invalid e-mail address"
        if len(postData['password']) < 8:
            errors['password'] = "Invalid passwprd"
        if postData['password'] != postData['con_password']:
            errors['match'] = "Passwords dont match"
        return errors
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
