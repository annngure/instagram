from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

#Create the forms

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username","email","password1","password2")
        
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['profile_image','bio']


class UpdateUser(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user','image']



       
