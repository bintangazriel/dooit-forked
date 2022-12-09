from django.http import HttpResponseRedirect
from kategori.models import Kategori
from kategori.forms import KategoriForm
from django.http.response import HttpResponse
from django.urls import reverse
from kategori.models import Kategori
from users.views import *
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required(login_url='/login/')
@user_passes_test(check_role_pencatat)
def index(request):
    kategoris_pemasukan = Kategori.objects.filter(user=request.user, jenis_kategori=1)
    kategoris_pengeluaran = Kategori.objects.filter(user=request.user, jenis_kategori=2)
    response = {'kategoris_pemasukan': kategoris_pemasukan, 'kategoris_pengeluaran':kategoris_pengeluaran}
    return render(request, 'kategori_index.html', response)

@login_required(login_url='/login/')
@user_passes_test(check_role_pencatat)
def buat_kategori(request):
    context = {}
  
    form = KategoriForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        kategori_form = form.save(commit=False)
        kategori_form.user = request.user
        kategori_form.save()
        messages.success(request, 'Kategori baru berhasil dibuat!')
        return HttpResponseRedirect(reverse('kategori:index'))
    
    elif form.errors:
        messages.error(request, 'Kategori ini sudah pernah dibuat!')
    
    context['form']= form
    return render(request, "buat_kategori.html", context)