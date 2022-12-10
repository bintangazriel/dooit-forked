from django.db import models
from konsultan.models import Konsultan
from users.models import CustomUser

# Create your models here.

class Konsultasi(models.Model):
    STATUS = (
        ('Menunggu Persetujuan', 'Menunggu Persetujuan'),
        ('Dibatalkan', 'Dibatalkan'),
        ('Disetujui', 'Disetujui'),
        ('Ditolak', 'Ditolak'),
        ('Sedang Berlangsung', 'Sedang Berlangsung'),
        ('Selesai', 'Selesai'),
    )

    klien = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    konsultan = models.ForeignKey(Konsultan, on_delete=models.CASCADE)
    status = models.CharField(max_length=25, choices=STATUS, default='Menunggu Persetujuan')
    alasan = models.TextField(verbose_name='Alasan Konsultasi')
    tanggal = models.DateField(verbose_name='Tanggal Konsultasi')
    tanggal_diajukan = models.DateTimeField(auto_now_add=True)
    tanggal_diubah = models.DateTimeField(auto_now=True)
    is_accepted = models.BooleanField(default=False)
    