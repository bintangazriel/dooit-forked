from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from catatanTransaksi.forms import CatatanTransaksiForm
from catatanTransaksi.models import CatatanTransaksi
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from kategori.models import Kategori
from users.views import check_role_pencatat
from django.http import JsonResponse
from django.contrib import messages

def get_saldo_by_jenis(pencatat, jenis):
    catatanTransaksis = CatatanTransaksi.objects.filter(pencatat=pencatat, jenis=jenis)
    return sum(map(lambda ct: ct.nominal, catatanTransaksis))
    
@login_required(login_url='login')
@user_passes_test(check_role_pencatat)
def index(request):
    catatanTransaksis = CatatanTransaksi.objects.filter(pencatat=request.user).order_by('-tanggal')
    saldoPemasukan = get_saldo_by_jenis(pencatat=request.user, jenis=1)
    saldoPengeluaran = get_saldo_by_jenis(pencatat=request.user, jenis=2)
    response = {
        'catatanTransaksis': catatanTransaksis,
        'totalSaldo': saldoPemasukan-saldoPengeluaran
    }
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
        messages.success(request, 'Catatan transaksi baru berhasil dibuat!')
        return HttpResponseRedirect(reverse('catatan-transaksi:index'))
    
    elif form.errors:
        messages.error(request, 'Isian formulir tidak valid!')

    context['form'] = form
    return render(request, "buat_catatan_transaksi.html", context)

def load_kategoris(request):
    jenis_kategori_id = request.GET.get('jenis')
    kategoris = Kategori.objects.filter(user=request.user, jenis_kategori_id=jenis_kategori_id)
    return render(request, 'kategori_dropdown_options.html', {'kategoris': kategoris})

def get_category(transaksi):
    s = set()
    for x in transaksi:
        s.add(x.kategori)
    return s

def get_time():    
    lst_month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return lst_month


def get_total_by_kategori(request, kategori,jenis):
    total = 0
    transaksi_kategori = CatatanTransaksi.objects.filter(pencatat=request.user, kategori=kategori,jenis=jenis)
    for item in transaksi_kategori:
        total += item.nominal
    return total

def get_total_by_waktu(request,tanggal,jenis):
    total = 0
    transaksi_tanggal = CatatanTransaksi.objects.filter(pencatat=request.user, tanggal__month=tanggal+1,jenis=jenis)
    for item in transaksi_tanggal:
        total += item.nominal
    return total

@login_required(login_url='login')
@user_passes_test(check_role_pencatat)
def view_laporan_keuangan(request):
  
    total_pemasukan = 0
    transaksi_pemasukan = CatatanTransaksi.objects.filter(pencatat=request.user, jenis=1)
    total_pengeluaran = 0
    transaksi_pengeluaran = CatatanTransaksi.objects.filter(pencatat=request.user, jenis=2)
    for item in transaksi_pemasukan:
        total_pemasukan += item.nominal

    for item in transaksi_pengeluaran:
        total_pengeluaran += item.nominal
    response = {
        'total_pemasukan':total_pemasukan,
        'total_pengeluaran':total_pengeluaran
    }
    return render(request,'visualisasi_laporan_keuangan.html',response)

def get_vis_pemasukan_pengeluaran_by_waktu(request):
    finalrep_pengeluaran = {}
    finalrep_pemasukan = {}  
    lst_time_label = get_time()
    for z in lst_time_label:
        finalrep_pemasukan[z] = get_total_by_waktu(request, lst_time_label.index(z),1)
        finalrep_pengeluaran[z] = get_total_by_waktu(request, lst_time_label.index(z),2)
    return JsonResponse({'expense_time_data': finalrep_pengeluaran,'income_time_data': finalrep_pemasukan}, safe=False)

def get_vis_pengeluaran_by_kategori(request):
    transaksi_pengeluaran = CatatanTransaksi.objects.filter(pencatat=request.user, jenis=2)
    finalrep_pengeluaran = {}
    lst_kategori_pengeluaran = get_category(transaksi_pengeluaran)
    for x in lst_kategori_pengeluaran:
        finalrep_pengeluaran[x.get_nama()] = get_total_by_kategori(request, x,2)
    return JsonResponse({'expense_category_data': finalrep_pengeluaran}, safe=False)