# from django.shortcuts import render

import logging

from django.http import HttpResponse
from profiles.forms import RegisterForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User


logger = logging.getLogger(__name__)


def profiles(request):...


def register(request):
   if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
     
            user = User(email=form.cleaned_data["email"])
            user.set_password(form.cleaned_data["password"])
            user.save()
            
            
            return redirect("login")
   else:
       form = RegisterForm()
   return render(request, "register.html", {"form": form})




def login_view(request):
   if request.method == "POST":
       form = LoginForm(request.POST)
       if form.is_valid():
           user = authenticate(request=request, **form.cleaned_data)
           if user is None:
               return HttpResponse('BadRequest', status=400)
           login(request, user)
           return redirect("index")
   else:
       form = LoginForm()
   return render(request, "login.html", {"form": form})

def logout_view(request):
   logout(request)
   return redirect("index")
