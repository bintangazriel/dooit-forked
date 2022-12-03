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
        return self.kategori
    