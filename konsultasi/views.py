from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

from .forms import KonsultasiForm
from .models import Konsultasi
from konsultan.models import Konsultan
from users.views import check_role_pencatat

# Create your views here.

@login_required(login_url='/login/')
@user_passes_test(check_role_pencatat)
def index(request):
    list_konsultasi = Konsultasi.objects.filter(klien=request.user)
    response = {
        'list_konsultasi': list_konsultasi
    }

    return render(request, 'konsultasi_index.html', response)


@login_required(login_url='/login/')
@user_passes_test(check_role_pencatat)
def pilih_konsultan(request):
    list_konsultan = Konsultan.objects.all()
    jumlah_konsultan = Konsultan.objects.count()
    response = {
        'list_konsultan': list_konsultan,
        'jumlah_konsultan': jumlah_konsultan
    }

    return render(request, 'konsultasi_selection.html', response)


@login_required(login_url='/login/')
@user_passes_test(check_role_pencatat)
def ajukan_konsultasi(request, konsultan_id):
    form = KonsultasiForm()
    konsultan = get_object_or_404(Konsultan, pk=konsultan_id)

    if request.method == 'POST':
        form = KonsultasiForm(request.POST)
        if form.is_valid():
            konsultasi = form.save(commit=False)
            konsultasi.klien = request.user
            konsultasi.konsultan = konsultan
            konsultasi.save()
            return redirect('/konsultasi')
    response = {
        'form': form,
        'konsultan': konsultan
    }

    return render(request, 'konsultasi_create.html', response)