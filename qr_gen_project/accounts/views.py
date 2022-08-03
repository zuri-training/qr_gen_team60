from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.decorators import unauthenticated_user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

from .forms import CreateUserForm

#===============================================================


# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')


# Registers a new user
@unauthenticated_user
def register(request):
  form = CreateUserForm()
    
  if request.method=='POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      
      messages.success(request," Account was Created for "+username)
      return redirect('accounts:login')
    else:
      messages.error(request, 'Incorrect credentials')
        
  context = {'form':form}
  return render(request,'accounts/register.html', context)


@unauthenticated_user
def login_view(request):
  """ This uses the built in Django User"""
  if request.method =='POST':
		
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      return redirect('qr_generator:home',) # pk=str(request.user.id)
      
    else: messages.error(request, 'Account not Registered!!')
  
  return render(request, 'accounts/login.html')


@login_required(login_url="/accounts/login")
def dashboard(request):
	context = {}
	return redirect('qr_generate:home')


@unauthenticated_user
def log_out(request):
	logout(request)
	messages.success(request, f'{request.user} Logged out')
	return HttpResponseRedirect(redirect_to='qr_generate:home')