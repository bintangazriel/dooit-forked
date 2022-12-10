from django import forms
from django.core import validators
from kategori.models import Kategori
from .models import CatatanTransaksi

class CatatanTransaksiForm(forms.ModelForm):
    class Meta:
        model = CatatanTransaksi
        fields = ['deskripsi', 'nominal', 'tanggal', "jenis", 'kategori']

        widgets = {   
            'deskripsi': forms.TextInput(
                attrs={'class': 'form-control', 
                    'placeholder': 'Masukkan deskripsi catatan transaksi',
                    'required':'true'
                    }),

            'nominal': forms.NumberInput(
                attrs={'class': 'form-control', 
                    'placeholder': 'Masukkan nominal catatan transaksi',
                    'required':'true',
                    'min': 0,
                    'type': 'number'
                    }),

            'tanggal': forms.DateInput(
                attrs={'class': 'form-control', 
                    'placeholder': 'Masukkan tanggal catatan transaksi',
                    'required':'true',
                    'type': 'date'
                    }),
            
            'jenis': forms.Select(
                        attrs={'class': 'form-select', 
                        'required':'true'
                        }),

            'kategori': forms.Select(
                        attrs={'class': 'form-select', 
                        'required':'true'
                        })
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['kategori'].queryset = Kategori.objects.none()

            if 'kategori' in self.data:
                try:
                    kategori_id = int(self.data.get('kategori'))
                    self.fields['kategori'].queryset = Kategori.objects.filter(kategori_id=kategori_id)
                except (ValueError, TypeError):
                    pass
            elif self.instance.pk:
                self.fields['kategori'].queryset = self.instance.jenis.kategori_set
