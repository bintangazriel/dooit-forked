from django import forms
from django.forms import widgets
from .models import Anggaran

class AnggaranForm(forms.ModelForm):
    class Meta:
        model = Anggaran
        fields = ['nominal', 'deskripsi', 'kategori', 'tanggal_mulai', 'tanggal_selesai']

        widgets = {
                    'nominal': forms.NumberInput(
                        attrs={'class': 'form-control',
                        'placeholder': 'Masukkan nominal anggaran',
                        'required':'true'
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
                        # format=('%d-%m-%Y'),
                        attrs={'class': 'form-control', 
                            'placeholder': 'Pilih tanggal anggaran dimulai',
                            'type': 'date',
                            'required':'true'
                            }),

                    'tanggal_selesai': forms.DateInput(
                        # format=('%d-%m-%Y'),
                        attrs={'class': 'form-control', 
                            'placeholder': 'Pilih tanggal anggaran selesai',
                            'type': 'date',
                            'required':'true'
                            })
        }