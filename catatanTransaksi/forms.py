from django import forms

from kategori.models import Kategori
from .models import CatatanTransaksi

class CatatanTransaksiForm(forms.ModelForm):
    class Meta:
        model = CatatanTransaksi
        fields = ['deskripsi', 'nominal', 'tanggal', "jenis", 'kategori']

        widgets = {
                    'tanggal': forms.DateInput(
                        format=('%Y-%m-%d'),
                        attrs={'class': 'form-control', 
                            'placeholder': 'Select a date',
                            'type': 'date'
                            })
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # self.fields['kategori'].queryset = Kategori.objects.none()

            if 'kategori' in self.data:
                try:
                    kategori_id = int(self.data.get('kategori'))
                    self.fields['kategori'].queryset = Kategori.objects.filter(kategori_id=kategori_id)
                except (ValueError, TypeError):
                    pass
            elif self.instance.pk:
                self.fields['kategori'].queryset = self.instance.jenis.kategori_set
