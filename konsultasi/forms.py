from django import forms
from .models import Konsultasi

class KonsultasiForm(forms.ModelForm):
    class Meta:
        model = Konsultasi
        fields = ['alasan', 'tanggal']
        widgets = {
          'alasan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan alasanmu mengajukan konsultasi'}),
          'tanggal': forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'form-control', 'placeholder': 'Pilih tanggal', 'type': 'date'})
        }