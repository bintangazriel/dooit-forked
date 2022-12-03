from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from catatanTransaksi.forms import CatatanTransaksiForm
from catatanTransaksi.models import CatatanTransaksi
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from kategori.models import Kategori
from users.views import check_role_pencatat
from django.http import JsonResponse
import datetime

@login_required(login_url='login')
@user_passes_test(check_role_pencatat)
def index(request):
    catatanTransaksis = CatatanTransaksi.objects.filter(pencatat=request.user)
    response = {'catatanTransaksis': catatanTransaksis}
    return render(request, 'catatan_transaksi_index.html', response)

@login_required(login_url='login')
@user_passes_test(check_role_pencatat)
def detail(request, id):
    catatanTransaksi = CatatanTransaksi.objects.get(pencatat=request.user, id=id)
    response = {'catatanTransaksi': catatanTransaksi}
    return render(request, 'detail_catatan_transaksi.html', response)

@login_required(login_url='login')
@user_passes_test(check_role_pencatat)
def buat(request):
    context = {}
  
    form = CatatanTransaksiForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        catatan_transaksi_baru = form.save(commit=False)
        catatan_transaksi_baru.pencatat = request.user
        catatan_transaksi_baru.save()
        return HttpResponseRedirect(reverse('buat_catatan_transaksi'))
    
    context['form'] = form
    return render(request, "buat_catatan_transaksi.html", context)

def load_kategoris(request):
    jenis_kategori_id = request.GET.get('jenis')
    kategoris = Kategori.objects.filter(jenis_kategori_id=jenis_kategori_id)
    return render(request, 'kategori_dropdown_options.html', {'kategoris': kategoris})

def get_vis_laporan_keuangan(request):
    todays_date = datetime.date.today()
    six_months_ago = todays_date-datetime.timedelta(days=30)
    transaksi = CatatanTransaksi.objects.filter(date__gte=six_months_ago, date__lte=todays_date)
    finalrep_pengeluaran = {}
    finalrep_pemasukan = {}

    def get_category(transaksi):
        return transaksi.kategori
    category_list = list(set(map(get_category, transaksi)))

    def get_nominal_pengeluaran(jenis):
        total_pengeluaran = 0
        filtered_by_jenis = transaksi.filter(jenis="Pengeluaran")

        for item in filtered_by_jenis:
            total_pengeluaran += item.nominal
        return total_pengeluaran
    
    def get_nominal_pemasukan(jenis):
        total_pemasukan = 0
        filtered_by_jenis = transaksi.filter(jenis="Pemasukan")

        for item in filtered_by_jenis:
            total_pemasukan += item.nominal
        return total_pemasukan

    for x in transaksi:
        for y in category_list:
            finalrep_pemasukan[y] = get_nominal_pemasukan(y)
            finalrep_pengeluaran[y] = get_nominal_pengeluaran(y)

    return JsonResponse({'expense_category_data': finalrep_pengeluaran,'income_category_data': finalrep_pemasukan}, safe=False)