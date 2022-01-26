from django.urls import path
from .views import PostListView, PostDetailView
from . import views


urlpatterns=[
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post_detail'),
    path('create-post/', views.create, name='create_post'),
    path('update-post/', views.update, name='update_post'),
    path('user_profile/', views.profile, name='user-profile'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about-us')
]