from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    context={
        "form":form}
    return render(request,'registration/register.html',context)

def loginPage(request):
    context={}
    return render(request,'registration/login.html',context)