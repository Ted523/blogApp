from django.shortcuts import render

posts = [
    {
        'author': 'Teddy Otieno',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 19, 2021'
    },
    
    {
        'author': 'Nova Waithaka',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 19, 2021'
    },

    {
        'author': 'Bridgit Wanyama',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'August 19, 2021'
    },

    {
        'author': 'Mercy Olorontubi',
        'title': 'Blog Post 4',
        'content': 'Fourth post content',
        'date_posted': 'September 19, 2021'
    },
]

# Create your views here.

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)

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