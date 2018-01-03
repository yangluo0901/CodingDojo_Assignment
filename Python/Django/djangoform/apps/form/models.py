# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import EmailValidator
from django.db import models
from django.core.exceptions import ValidationError

# from django.core.exceptions import ValidationError
# Create your models here.
def namelen_validator(value):
    if len(value) < 3 :
        raise ValidationError(" Name muset be longer than 3")

class User(models.Model):
    name = models.CharField(max_length = 50, validators = [namelen_validator])
    email = models.EmailField(max_length = 100)
    gender = models.CharField(max_length = 6, null = True)
