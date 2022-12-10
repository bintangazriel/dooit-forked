from django import forms
from kategori.models import Kategori

class KategoriForm(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = ['nama', 'jenis_kategori']
        widgets = {
          'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan nama kategori di sini'}),
          'jenis_kategori': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Pilih jenis kategori di sini'})
        }