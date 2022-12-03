from django.db import models
from django.db.models.fields.related import ForeignKey
from users.models import CustomUser

class Anggaran(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    nominal = models.FloatField(verbose_name="Jumlah Anggaran", null=True, blank=True)
    deskripsi = models.CharField(verbose_name="Deskripsi Anggaran", null=True, blank=True, max_length = 30)
    # kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    kategori = models.CharField(verbose_name="Kategori Anggaran", null=True, blank=True, max_length = 30)
    tanggal_mulai = models.DateField()
    tanggal_selesai = models.DateField()