from django import forms
from .models import *
from django.core.exceptions import ValidationError
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        print " i am here "
    def clean_email(self):
        email = self.cleaned_data['email']
        print email
        if not "edu" in email:
            print "i am here1"
            raise forms.ValidationError("invalid email")
        return email
