from django.urls import path
from anggaran.views import buat_anggaran, index

app_name = "anggaran"

urlpatterns = [
    path('', index, name='index'),
    path('buat-anggaran', buat_anggaran, name='buat_anggaran'),
]