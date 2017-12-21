# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # validate first name:
        if postData['first_name'].isalpha():
            if len(postData['first_name']) < 3:
                errors['first_name'] =  " first name is too short"
        else:
            errors['first_name'] = " Number should not be inside the name"
            if len(postData['first_name']) < 3:
                errors['first_name'] += ", first name is too short "
        #validate last name:
        if postData['last_name'].isalpha():
            if len(postData['last_name']) < 2:
                errors['last_name'] =  " last name is too short"
        else:
            errors['last_name'] = " Number should not be inside the name"
            if len(postData['last_name']) < 2:
                errors['last_name'] += ", last name is too short "
        # validate email:
        if not email_regex.match(postData['email']):
            errors['email'] = "invalid e-mail"
        return errors
class User(models.Model):
    first_name  = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
