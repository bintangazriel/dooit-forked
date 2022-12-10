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
    messages.warning(request, 'Anda sudah berada di dalam sistem!')
    return redirect('/')
  elif request.method == 'POST':
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
      messages.success(request, 'Akun Anda telah berhasil didaftarkan!')
      return redirect('login')
    else:
      messages.error(request, 'Form tidak valid. Silakan coba lagi!')
      return redirect('register')
  else:
    form = UserForm()
  
  context = {
    'form': form,
  }

  return render(request, 'register.html', context)


def login(request):
  if request.user.is_authenticated:
    messages.warning(request, 'Anda sudah berada di dalam sistem!')
    return redirect('/')
  elif request.method == 'POST':
    email = request.POST['email']
    password = request.POST['password']

    user = auth.authenticate(email=email, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'Anda berhasil masuk ke dalam sistem!')
      return redirect('/')
    else:
      messages.error(request, 'Informasi login yang Anda masukkan salah!')
      return redirect('login')

  return render(request, 'login.html')


def logout(request):
  auth.logout(request)
  messages.info(request, 'Anda telah berhasil keluar')
  return redirect('login')