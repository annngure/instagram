from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm
from django.contrib import messages
from .models import *

# Create your views here.



def index(request):

    context={}
    return render(request,'index.html',context)

@login_required(login ='/registration/login/')
def profileView(request):
    current_user = request.user
    profile = profile.objects.all()
    context={
        "current_user":current_user
        "profile":profile
    }
    return render(request, 'profile.html',context)

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