from django.urls import path
from kategori.views import *

app_name = "kategori"

urlpatterns = [
    path('', index, name='index'),
    path('buat-kategori/', buat_kategori, name='buat_kategori'),
]