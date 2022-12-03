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
    