from django import forms
from django.forms import widgets
from .models import Anggaran
from django.core.exceptions import ValidationError
import datetime

class AnggaranForm(forms.ModelForm):
    def clean_tanggal_mulai(self):
        data = self.cleaned_data['tanggal_mulai']

        if data < datetime.date.today():
            raise ValidationError("Tanggal yang dimasukkan tidak boleh lampau")

        return data

    def clean_tanggal_selesai(self):
        data = self.cleaned_data['tanggal_selesai']

        if data < datetime.date.today():
            raise ValidationError("Tanggal yang dimasukkan tidak boleh lampau")

        return data

    class Meta:
        model = Anggaran
        fields = ['nominal', 'deskripsi', 'kategori', 'tanggal_mulai', 'tanggal_selesai']

        widgets = {
                    'nominal': forms.NumberInput(
                        attrs={'class': 'form-control',
                        'placeholder': 'Masukkan nominal anggaran',
                        'required':'true',
                        'min':0
                        }),

                    'deskripsi': forms.TextInput(
                        attrs={'class': 'form-control',
                        'placeholder': 'Masukkan deskripsi anggaran',
                        'required':'true'
                        }),

                    'kategori': forms.Select(
                        attrs={'class': 'form-select', 
                        'placeholder': 'Pilih kategori anggaran',
                        'required':'true'
                        }),

                    'tanggal_mulai': forms.DateInput(
                        attrs={'class': 'form-control', 
                            'placeholder': 'Pilih tanggal anggaran dimulai',
                            'type': 'date',
                            'required':'true'
                            }),

                    'tanggal_selesai': forms.DateInput(
                        attrs={'class': 'form-control', 
                            'placeholder': 'Pilih tanggal anggaran selesai',
                            'type': 'date',
                            'required':'true'
                            })
        }