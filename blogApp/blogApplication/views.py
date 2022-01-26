from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost

# Create your views here.

# def home(request):
#     context = {
#         'posts': BlogPost.objects.all()
#     }
#     return render(request, 'home.html', context)

class PostListView(ListView):
    model = BlogPost
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = BlogPost
    context_object_name = 'post' 

def create(request):
    return render(request, 'create_post.html')

def details(request):
    context = {
        'post': BlogPost.objects.all()
    }
    return render(request, 'post_detail.html', context)

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