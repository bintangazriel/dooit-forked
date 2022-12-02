from django.urls import path
from anggaran.views import buat_anggaran, index

urlpatterns = [
    path('', index, name='index'),
    path('buat-anggaran', buat_anggaran, name='buat_anggaran'),
]