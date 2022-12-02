from django.db import models

# Create your models here.
class Anggaran(models.Model):
    nominal = models.FloatField(verbose_name="Jumlah Anggaran", null=True, blank=True)
    deskripsi = models.CharField(verbose_name="Deskripsi Anggaran", null=True, blank=True, max_length = 30)
    # kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    kategori = models.CharField(verbose_name="Kategori Anggaran", null=True, blank=True, max_length = 30)
    tanggal_mulai = models.DateField()
    tanggal_selesai = models.DateField()