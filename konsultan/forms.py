from django import forms
from .models import Konsultan


class KonsultanForm(forms.ModelForm):
  class Meta:
    model = Konsultan
    fields = ['first_name', 'last_name']