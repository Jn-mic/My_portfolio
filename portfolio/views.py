from django.shortcuts import render
from django.http import HttpResponse
import sys
sys.path.append("..")
# from users.models import User
from django.http import HttpResponse
from django.views import generic 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# from .email import send_welcome_email
import datetime as dt

# Create your views here.
def Home(request):

    return render(request,'portfolio/home.html')

# def HomePageView(request):
#     return render(request,'portfolio/home.html')