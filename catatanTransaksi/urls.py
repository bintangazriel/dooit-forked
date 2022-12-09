from django.urls import path
from catatanTransaksi.views import buat, index, detail, load_kategoris, get_vis_pengeluaran_by_kategori, view_laporan_keuangan, get_vis_pemasukan_pengeluaran_by_waktu

urlpatterns = [
    path('', index, name='index'),
    path('buat', buat, name='buat_catatan_transaksi'),
    path('detail/<int:id>', detail, name='detail_catatan_transaksi'),
    path('ajax/load-kategoris/', load_kategoris, name='ajax_load_kategoris'),
    path('get_vis_pengeluaran_by_kategori', get_vis_pengeluaran_by_kategori, name='get_vis_pengeluaran_by_kategori'),
    path('get_vis_pemasukan_pengeluaran_by_waktu', get_vis_pemasukan_pengeluaran_by_waktu, name='get_vis_pemasukan_pengeluaran_by_waktu'),
    path('view',view_laporan_keuangan, name='view')
]