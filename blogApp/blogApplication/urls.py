from django.urls import path
from . import views


urlpatterns=[
    path('', views.home, name='home'),
    path('create-post/', views.create, name='create_post'),
    path('post-detail/', views.details, name = 'post_detail'),
    path('update-post/', views.update, name='update_post'),
    path('user_profile/', views.profile, name='user-profile'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about-us')
]