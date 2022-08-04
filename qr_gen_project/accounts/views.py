from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.decorators import unauthenticated_user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

from .forms import CreateUserForm

#===============================================================
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes


#=================================================================

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')


# Registers a new user
@unauthenticated_user
def register(request):
    
  if request.method=='POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      
      login(request, username)
      messages.success(request," Account was Created for "+username)
      return redirect('accounts:home')
  
    messages.error(request, 'Incorrect credentials')
  form = CreateUserForm()
        
  context = {'form':form}
  return render(request,'accounts/register.html', context)


from django.contrib.auth.forms import AuthenticationForm #add this

@unauthenticated_user
def login_view(request):
  """ This uses the built in Django User"""
  context = {}

  if request.method =='POST':
    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)

      if user is not None:
        login(request, user)
        messages.info(request, f"You are now logged in as {username}.")
        return redirect('qr_generator:home',) # pk=str(request.user.id)
        
      else: messages.error(request, 'Account not Registered!!')
    
    else:
      messages.error(request, "Invalid Username or Password")

  form = AuthenticationForm()   
  context['form'] = form 
  return render(request, 'accounts/login.html', context)


@login_required(login_url="/accounts/login")
def dashboard(request):
	context = {}
	return redirect('qr_generator:home')


@unauthenticated_user
def log_out(request):
	logout(request)
	messages.success(request, f'{request.user} Logged out')
	return HttpResponseRedirect(redirect_to='qr_generate:home')



def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "accounts/password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',#!
					'site_name': 'Website',#!
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',#!
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'simplenicky1@gmail.com' , [user.email], fail_silently=False) #! change admin later
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ('accounts:password_reset_done')#!
	password_reset_form = PasswordResetForm()
  
	return render(request=request, template_name="accounts/password/password_reset.html", context={"password_reset_form":password_reset_form},)