from django.shortcuts import render
from django.http import HttpResponse
import sys
sys.path.append("..")


import datetime as dt

# Create your views here.
def home(request):

    return render(request,'portfolio/home.html')

def about(request):

    return render(request,'portfolio/aboutme.html')

def hire(request):

    return render(request,'portfolio/hireme.html')

def project(request):

    return render(request,'portfolio/myproject.html')

def contact(request):

    return render (request,'portfolio/contact.html')

