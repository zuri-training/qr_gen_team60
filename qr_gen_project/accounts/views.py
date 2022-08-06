from .imports import *


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
      email = form.cleaned_data.get('email')
      
      login(request, email)
      messages.success(request," Account was Created for "+email)
      return redirect('accounts:home')
  
    messages.error(request, 'Incorrect credentials')
  form = CreateUserForm()
        
  context = {'form':form}
  return render(request,'accounts/signup.html', context)


from django.contrib.auth.forms import AuthenticationForm #add this

@unauthenticated_user
def login_view(request):
  """ This uses the built in Django User"""
  context = {}

  if request.method =='POST':
    email = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=email, password=password)

    print(email, password)

    if user is not None:
      login(request, user)
      print(f'{user} logged in')
      messages.success(request, f"You are now logged in as {email}.")
      return redirect('qr_generator:home',) # pk=str(request.user.id)
      
    else: 
      messages.error(request, 'Account not Registered!!')
      print(user)
  
  return render(request, 'accounts/login.html', context)


@login_required(login_url="/qr-gen/accounts/login")
def dashboard(request):
	context = {}
	return redirect('qr_generator:home')


@login_required(login_url="/qr-gen/accounts/login")
def log_out(request):
	logout(request)
	messages.success(request, f'{request.user} Logged out')
	return redirect(to='qr_generator:home')


@login_required(login_url="/qr-gen/accounts/login")
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