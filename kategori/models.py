from django.db import models
from django.db.models.fields.related import ForeignKey
from users.models import CustomUser
from catatanTransaksi.models import *

class Kategori(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=30, unique=True)
    jenis_kategori = models.ForeignKey(JenisTransaksi, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nama

    def get_nama(self):
        return self.nama

    def get_list_catatan_transaksi(self):
        return Kategori.objects.get(nama=self.nama).catatantransaksi_set.all()

    def get_kategori_nomimal(self, start_date, end_date):
        catatan_transaksi = self.get_list_catatan_transaksi()
        nominal = 0

        for catatan in catatan_transaksi:
            if catatan.tanggal >= start_date and catatan.tanggal <= end_date:
                nominal = nominal + catatan.nominal
        return nominal