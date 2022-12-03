from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from catatanTransaksi.forms import CatatanTransaksiForm
from catatanTransaksi.models import CatatanTransaksi
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from users.views import check_role_pencatat
from django.http import JsonResponse
import datetime

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

def get_category(transaksi):
    s = set()
    for x in transaksi:
        s.add(x.kategori)
    return s


def get_total(transaksi,kategori):
    total = 0
    transaksi_kategori = transaksi.objects.filter(kategori=kategori)
    
    for item in transaksi_kategori:
        total += item.nominal
    return total


def get_vis_laporan_keuangan(request):
    todays_date = datetime.date.today()
    six_months_ago = todays_date-datetime.timedelta(days=30)
    transaksi_pemasukan = CatatanTransaksi.objects.filter(jenis="Pemasukan",date__gte=six_months_ago, date__lte=todays_date)
    transaksi_pengeluaran = CatatanTransaksi.objects.filter(jenis="Pengeluaran",date__gte=six_months_ago, date__lte=todays_date)
    finalrep_pengeluaran = {}
    finalrep_pemasukan = {}

    lst_kategori_pemasukan = get_category(transaksi_pemasukan)
    lst_kategori_pengeluaran = get_category(transaksi_pengeluaran)
    
    for y in lst_kategori_pemasukan:
        finalrep_pemasukan[y.get_nama()] = get_total(transaksi_pemasukan,y)

    for x in lst_kategori_pengeluaran:
        finalrep_pengeluaran[x.get_nama()] = get_total(transaksi_pengeluaran,x)      

    return JsonResponse({'expense_category_data': finalrep_pengeluaran,'income_category_data': finalrep_pemasukan}, safe=False)