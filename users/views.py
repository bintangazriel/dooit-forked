from django.core.exceptions import PermissionDenied
from django.contrib import auth, messages
from django.shortcuts import redirect, render

from .forms import UserForm
from .models import CustomUser, CustomUserProfile

# Create your views here.

# Membatasi konsultan untuk mengakses halaman pencatat
def check_role_pencatat(user):
  if user.role == 1:
    return True
  else:
    raise PermissionDenied


# Membatasi pencatat untuk mengakses halaman konsultan
def check_role_konsultan(user):
  if user.role == 2:
    return True
  else:
    raise PermissionDenied


def register(request):
  if request.user.is_authenticated:
    messages.warning(request, 'You are already logged in!')
    return redirect('/')
  elif request.POST == 'POST':
    form = UserForm(request.POST)

    if form.is_valid():
      # Create the user using create_user method from CustomUser class
      company_name = form.cleaned_data['company_name']
      username = form.cleaned_data['username']
      email = form.cleaned_data['email']
      password = form.cleaned_data['password']
      user = CustomUser.objects.create_user(company_name=company_name, username=username, email=email, password=password)
      user.role = CustomUser.PENCATAT
      user.save()
      messages.success(request, 'Your account has been registered sucessfully!')
      return redirect('/')
  
  else:
    form = UserForm()
  
  context = {
    'form': form,
  }

  return render(request, 'register.html', context)


def login(request):
  if request.user.is_authenticated:
    messages.warning(request, 'You are already logged in!')
    return redirect('/')
  elif request.method == 'POST':
    email = request.POST['email']
    password = request.POST['password']

    user = auth.authenticate(email=email, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in.')
      return redirect('/')
    else:
      messages.error(request, 'Invalid login credentials')
      return redirect('login')
  return render(request, 'login.html')


def logout(request):
  auth.logout(request)
  messages.info(request, 'You are logged out.')
  return redirect('login')