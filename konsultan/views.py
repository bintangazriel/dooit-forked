from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Konsultan
from konsultasi.models import Konsultasi
from users.views import check_role_konsultan
# Create your views here.

@login_required(login_url='/login/')
@user_passes_test(check_role_konsultan)
def dashboard_konsultan(request):
    list_konsultasi = Konsultasi.objects.filter(konsultan=request.user).order_by('tanggal_diajukan')
    response = {
        'list_konsultasi': list_konsultasi
    }
    
    return render(request, 'dashboard_konsultan.html', response)


@login_required(login_url='/login/')
@user_passes_test(check_role_konsultan)
def profil_konsultan(request):
    konsultan = Konsultan.objects.get(konsultan=request.user)
    response = {
        'konsultan': konsultan
    }
    return render(request, 'profil_konsultan.html', response)