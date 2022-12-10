from django import forms
from django.core.exceptions import ValidationError
from .models import Konsultasi
import datetime

class KonsultasiForm(forms.ModelForm):
    class Meta:
        model = Konsultasi
        fields = ['alasan', 'tanggal']
        widgets = {
          'alasan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan alasanmu mengajukan konsultasi'}),
          'tanggal': forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'form-control', 'placeholder': 'Pilih tanggal', 'type': 'date'})
        }
    
    def clean_tanggal(self):
        data = self.cleaned_data['tanggal']

        if data < datetime.date.today():
            raise ValidationError("Tanggal yang dimasukkan tidak boleh tanggal yang sudah lampau")

        return data