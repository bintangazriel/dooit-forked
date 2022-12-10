from django.urls import path

from konsultan.views import terima_konsultasi, tolak_konsultasi
from .views import index, ajukan_konsultasi, pilih_konsultan

app_name = 'konsultasi'

urlpatterns = [
    path('', index, name='index'),
    path('pick-consultant/', pilih_konsultan, name='pilih_konsultan'),
    path('pick-consultant/<int:konsultan_id>/create/', ajukan_konsultasi, name='ajukan_konsultasi'),
    path('<int:konsultasi_id>/accept-request/', terima_konsultasi, name='terima_konsultasi'),
    path('<int:konsultasi_id>/deny-request/', tolak_konsultasi, name='tolak_konsultasi'),
]