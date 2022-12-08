from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

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


def pilih_konsultan(request):
    list_konsultan = Konsultan.objects.all()
    jumlah_konsultan = Konsultan.objects.count()
    response = {
        'list_konsultan': list_konsultan,
        'jumlah_konsultan': jumlah_konsultan
    }
    return render(request, 'konsultasi_selection.html', response)


def ajukan_konsultasi(request, konsultan_id):
    konsultan = get_object_or_404(Konsultan, pk=konsultan_id)
    return render(request, 'konsultasi_create.html')