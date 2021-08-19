from django.shortcuts import render

from django.http import HttpResponse

import datetime

# Create your views here.
posts = [{'author':'Kevin Wesonga', 'title':'Fundamentals of Django','description':'Learn the 123s of Django web framework','category':'Technology'}, {'author':'Brian Kimani','title':'Affordable Domestic Travel','description':'Travel across Kenya with great deals','category':'Travel'}, {'author':'Wambui Oketch','title':'Styling your website with Flexbox','description':'Learn how to use Flexbox layout effectively','category':'Technology'}, {'author':'Musungu Sasha','title':'Minimalist Designs','description':'Exploring minimalism in design and architecture','category':'Art and Design'}, {'author':'Ali Noor','title':'A Brief History of Lamu','description':'Exploring the history of the Swahili Coast and Lamu Town','category':'History'}]

# titles = [post['title'] for post in posts]
# authors = [post['author'] for post in posts]
# categories = [post['category'] for post in posts]
# descriptions = [post['description'] for post in posts]



def home(request):
    return render(request, 'home.html', {
        'posts' : posts
    })

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

def about(request):
    return render(request, 'about.html')