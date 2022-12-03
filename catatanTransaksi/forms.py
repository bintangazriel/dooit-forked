from django import forms
from django.forms import widgets
from .models import CatatanTransaksi

class CatatanTransaksiForm(forms.ModelForm):
    class Meta:
        model = CatatanTransaksi
        fields = "__all__"

        widgets = {
                    'tanggal': forms.DateInput(
                        format=('%Y-%m-%d'),
                        attrs={'class': 'form-control', 
                            'placeholder': 'Select a date',
                            'type': 'date'
                            })
        }
