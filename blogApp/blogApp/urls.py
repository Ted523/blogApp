"""blogApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Accounts import views as account_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', account_views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='Accounts/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='Accounts/logout.html'), name="logout"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='Accounts/password_reset.html'), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='Accounts/password_reset_done.html'), name="password_reset_done"),

    path('', include("blogApplication.urls")),	
]
