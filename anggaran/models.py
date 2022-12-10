from django.db import models
from django.db.models.fields.related import ForeignKey, OneToOneField
from users.models import CustomUser
from kategori.models import Kategori

class Anggaran(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    nominal = models.FloatField(verbose_name="Jumlah Anggaran", null=True, blank=True)
    deskripsi = models.CharField(verbose_name="Deskripsi Anggaran", null=True, blank=True, max_length = 30)
    kategori = models.OneToOneField(Kategori, on_delete=models.CASCADE, null=True)
    tanggal_mulai = models.DateField()
    tanggal_selesai = models.DateField()

    def __str__(self):
        return self.kategori.get_nama()

    def get_pengeluaran(self):
        return self.kategori.get_kategori_nomimal(self.tanggal_mulai, self.tanggal_selesai)

    def get_sisa(self):
        return self.nominal - self.get_pengeluaran()

    def get_persentase(self):
        return int((self.nominal - self.get_sisa())/self.nominal * 100)
    