from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Konsultan
from konsultasi.models import Konsultasi
from users.views import check_role_konsultan

# Create your views here.

@login_required(login_url='/login/')
@user_passes_test(check_role_konsultan)
def dashboard_konsultan(request):
    konsultan = Konsultan.objects.get(user=request.user)
    list_konsultasi = Konsultasi.objects.filter(konsultanin=[konsultan.id], status='Menunggu Persetujuan')
    konsultasi_berlangsung = Konsultasi.objects.filter(konsultanin=[konsultan.id], is_accepted=True)

    response = {
        'list_konsultasi': list_konsultasi,
        'konsultasi_berlangsung': konsultasi_berlangsung
    }

    return render(request, 'konsultan_dashboard.html', response)


@login_required(login_url='/login/')
@user_passes_test(check_role_konsultan)
def terima_konsultasi(request, konsultasi_id):
    try:
        konsultasi = Konsultasi.objects.get(pk=konsultasi_id)
    except:
        konsultasi = None

    if konsultasi is not None:
        konsultasi.is_accepted = True
        konsultasi.status = 'Disetujui'
        konsultasi.save()
        return redirect('/konsultan/dashboard')


@login_required(login_url='/login/')
@user_passes_test(check_role_konsultan)
def tolak_konsultasi(request, konsultasi_id):
    try:
        konsultasi = Konsultasi.objects.get(pk=konsultasi_id)
    except:
        konsultasi = None

    if konsultasi is not None:
        konsultasi.status = 'Ditolak'
        konsultasi.save()
        return redirect('/konsultan/dashboard')