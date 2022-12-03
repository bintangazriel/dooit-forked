from django.db import models

# Create your models here.
class CatatanTransaksi(models.Model):
    deskripsi = models.CharField(verbose_name="Deskripsi Transaksi", null=True, blank=True, max_length = 30)
    nominal = models.FloatField(verbose_name="Jumlah Transaksi", null=True, blank=True)
    tanggal = models.DateField(verbose_name="Tanggal Transaksi")
    # kategori = models.ForeignKey(Kategori, on_delete=models.RESTRICT)
    kategori = models.CharField(verbose_name="Kategori Transaksi", null=True, blank=True, max_length = 30)
    # pencatat_keuangan = models.ForeignKey(PencatatKeuangan, on_delete=models.CASCADE)
    pencatat_keuangan = models.CharField(verbose_name="Pencatat Keuangan", null=True, blank=True, max_length = 30)
    # laporan_keuangan = models.ForeignKey(LaporanKeuangan, on_delete=models.CASCADE)
    laporan_keuangan = models.CharField(verbose_name="Laporan Keuangan", null=True, blank=True, max_length = 30)
    # jenis = models.ForeignKey(Jenis, on_delete=models.RESTRICT)
    jenis = models.CharField(verbose_name="Jenis Transaksi", null=True, blank=True, max_length = 30)