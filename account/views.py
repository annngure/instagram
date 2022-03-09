from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from .models import *

# Create your views here.



def index(request):

    context={}
    return render(request,'index.html',context)

@login_required()
def profileView(request):
    context={}
    return render(request, 'profile.html',context)

@login_required()
def update_profile(request):
    context={}
    if request.method =="POST":
        form = UpdateProfileForm(request.POST)
        if form.is_valid():
            request_profile.profile_image = form.cleaned_data['profile_image']
            request_profile.bio = form.cleaned_data['bio']
            request_profile.username = form.cleaned_data['username']
            request_profile.save_profile()
            return redirect('profile')
    else:
        form =UpdateProfileForm()
    if request.method =='POST':
        form = UpdateProfileForm(request.POST)
        if form.is_valid():
            new_profile = profile(profile_image = ['profile_image'],bio = form.cleaned_data['bio'],username = form.cleaned_data['username'])
            new_profile.save_profile()
            return redirect('profile')
    else:
        form = UpdateProfileForm()
    context={
        "form":form
    }

    return render(request, 'update-profile.html',context)



def registerView(request):
    if request.method=="POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"Registration sucessful.")
            return redirect('login')   
    else:
        messages.error(request,"Invalid Information")
        form = NewUserForm()
    context={
        "form":form}
    return render(request,'registration/register.html',context)

def loginPage(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username =form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.info(request,"You are now logged as {username}.")
                return redirect('profile')
            
    else:
        messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    context={
        "form":form
    }
    return render(request,'registration/login.html',context)

