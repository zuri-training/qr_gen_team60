from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from pkg_resources import require
from .models import Qr_Collection
from django import forms
from django.contrib.auth import login, logout

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
            return redirect('accounts:login')
        else:
            form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('accounts:dashboard')
        else:
            form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

@login_required(login_url="/accounts/login")
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout(request):
    if request.method == 'POST':
        logout(request)
    return render(request, 'accounts/logout.html')

@login_required(login_url="/accounts/login")
def faq(request):
    return redirct(request, 'accounts:faq')
     