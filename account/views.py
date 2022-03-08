from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm
from django.contrib import messages

# Create your views here.

# from .models import *

def index(request):
    context={}
    return render(request,'index.html',context)

@login_required
def profileView(request):
    return render(request, 'profile.html')

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
                return redirect("profile")
            else:
                messages.error(request,"Invalid username or password")
    else:
        messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    context={
        "form":form
    }
    return render(request,'registration/login.html',context)