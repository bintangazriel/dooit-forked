from django.db import models

from users.models import CustomUser

# Create your models here.


class JenisTransaksi(models.Model):
    PEMASUKAN = 1
    PENGELUARAN = 2
    PILIHAN_JENIS = ((PEMASUKAN,"Pemasukan"),(PENGELUARAN,"Pengeluaran"))
    jenis = models.PositiveSmallIntegerField(choices=PILIHAN_JENIS)

    def __str__(self):
        if self.jenis == 1:
            jenis = 'Pemasukan'
        elif self.jenis == 2:
            jenis = 'Pengeluaran'
        return jenis


class CatatanTransaksi(models.Model):
    deskripsi = models.CharField(verbose_name="Deskripsi Transaksi", null=True, blank=True, max_length = 30)
    nominal = models.FloatField(verbose_name="Jumlah Transaksi", null=True, blank=True)
    tanggal = models.DateField(verbose_name="Tanggal Transaksi")
    # kategori = models.ForeignKey(Kategori, on_delete=models.RESTRICT)
    # kategori = models.CharField(verbose_name="Kategori Transaksi", null=True, blank=True, max_length = 30)
    pencatat = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    jenis = models.ForeignKey(JenisTransaksi, on_delete=models.RESTRICT)