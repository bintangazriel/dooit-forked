from django.db import models


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
    pencatat = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    deskripsi = models.CharField(verbose_name="Deskripsi Transaksi", null=True, blank=True, max_length = 30)
    nominal = models.FloatField(verbose_name="Jumlah Transaksi")
    tanggal = models.DateField(verbose_name="Tanggal Transaksi")
    kategori = models.ForeignKey('kategori.Kategori', on_delete=models.RESTRICT)
    jenis = models.ForeignKey(JenisTransaksi, on_delete=models.RESTRICT)

    def get_tanggal(self):
        return self.tanggal