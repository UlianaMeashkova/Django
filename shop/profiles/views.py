# from django.shortcuts import render

import logging

from django.http import HttpResponse
from profiles.forms import RegisterForm
from django.shortcuts import render, redirect

logger = logging.getLogger(__name__)


def profiles(request):...


def register(request):
   if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
     
            logger.info(f"User email: {form.cleaned_data['email']}")
            logger.info(f"User password: {form.cleaned_data['password']}")
            
            
            return redirect("/thanks/")
   else:
       form = RegisterForm()
   return render(request, "register.html", {"form": form})


# Create your views here.
