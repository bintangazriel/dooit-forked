from django.urls import path
from catatanTransaksi.views import buat, index

urlpatterns = [
    path('', index, name='index'),
    path('buat', buat, name='buat_catatan_transaksi'),
]