from django.db import models

# Create your models here.
class Kategori(models.Model):
    user = models.ForeignKey
    kategori = models.CharField(max_length=15, unique=True, default='')
    jenis_transaksi = models.ForeignKey(JenisTransaksi, n_delete=models.CASCADE, null=True, default='')
    icon = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)