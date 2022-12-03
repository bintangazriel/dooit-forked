from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from catatanTransaksi.forms import CatatanTransaksiForm
from catatanTransaksi.models import CatatanTransaksi
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from users.views import check_role_pencatat

# Create your views here.
@login_required(login_url='login')
@user_passes_test(check_role_pencatat)
def index(request):
    # catatanTransaksis = CatatanTransaksi.objects.filter(pencatat_keuangan=request.user)
    catatanTransaksis = CatatanTransaksi.objects.all().values()
    response = {'catatanTransaksis': catatanTransaksis}
    return render(request, 'catatan_transaksi_index.html', response)

@login_required(login_url='login')
@user_passes_test(check_role_pencatat)
def detail(request):
    # catatanTransaksis = CatatanTransaksi.objects.filter(pencatat_keuangan=request.user)
    pass

@login_required(login_url='login')
@user_passes_test(check_role_pencatat)
def buat(request):
    context = {}
  
    form = CatatanTransaksiForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        catatan_transaksi_baru = form.save(commit=False)
        # catatan_transaksi_baru.pencatat_keuangan = request.user
        return HttpResponseRedirect(reverse('buat_catatan_transaksi'))
    
    context['form'] = form
    return render(request, "buat_catatan_transaksi.html", context)