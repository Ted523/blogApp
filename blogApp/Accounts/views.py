from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.
def register(request):
    # if request.method == 'post':
    form = UserCreationForm(request.post)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        messages.success(request, f'{username}, your account has been created successfully!')
        return redirect('home')
    else:
        messages.danger(request, 'Form is invalid')
    return render(request, 'Accounts/register.html', {'forms': form})
    