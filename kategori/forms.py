from django import forms
from models import Kategori

kategori_list = Kategori.objects.all()

class KategoriForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(KategoriForm, self).__init__(*args, **kwargs)

        self.fields['nama_kategori'] = forms.CharField(widget=forms.widgets.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nama',
            'type' : 'text',
            'required': True,
        }))

        self.fields['selectedImage'] = forms.ChoiceField(choices=kategori_list)