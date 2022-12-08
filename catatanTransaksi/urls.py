from django.urls import path
from catatanTransaksi.views import buat, index, detail, load_kategoris, get_vis_laporan_keuangan, view_laporan_keuangan

urlpatterns = [
    path('', index, name='index'),
    path('buat', buat, name='buat_catatan_transaksi'),
    path('detail/<int:id>', detail, name='detail_catatan_transaksi'),
    path('ajax/load-kategoris/', load_kategoris, name='ajax_load_kategoris'),
    path('get_laporan_keuangan', get_vis_laporan_keuangan, name='get_laporan_keuangan'),
    path('view',view_laporan_keuangan, name='view')
]