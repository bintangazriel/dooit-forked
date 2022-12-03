from django.urls import path
from catatanTransaksi.views import buat, index, detail, load_kategoris

urlpatterns = [
    path('', index, name='index'),
    path('buat', buat, name='buat_catatan_transaksi'),
    path('detail/<int:id>', detail, name='detail_catatan_transaksi'),
    path('ajax/load-kategoris/', load_kategoris, name='ajax_load_kategoris'),
]