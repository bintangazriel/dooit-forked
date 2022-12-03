from django import forms
from kategori.models import Kategori

class KategoriForm(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = ['nama', 'jenis_kategori']