from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# from .models import Qr_Collection
from django import forms
from accounts.decorators import unauthenticated_user

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your registration is successful.')
            return redirect('login')
        else:
            form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})

def login(request):
    return render(request, 'accounts/login.html')

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout(request):
    return render(request, 'accounts/logout.html')
     
@unauthenticated_user
def login(request):
    return render(request,  'accounts/register.html')