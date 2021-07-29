from django.shortcuts import render

from django.http import HttpResponse

import datetime

# Create your views here.

def home(request):
    return render(request, 'home.html')

def create(request):
    return render(request, 'create_post.html')

def details(request):
    return render(request, 'post_detail.html')

def update(request):
    return render(request, 'update_post.html')

def profile(request):
    return render(request, 'user_profile.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')