# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .form import UserForm
from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
# Create your views here.
def index(request):
    # if request.method == "POST":
        bound_form = UserForm(request.POST)
        print bound_form.is_valid()
        if bound_form.is_valid():
            bound_form.save()
        return render (request, 'form/index.html',{'form':bound_form})
