from django.urls import path
from .views import index, ajukan_konsultasi, pilih_konsultan

app_name = 'konsultasi'

urlpatterns = [
    path('', index, name='index'),
    path('pick-consultant/', pilih_konsultan, name='pilih_konsultan'),
    path('pick-consultant/<int:konsultan_id>/create/', ajukan_konsultasi, name='ajukan_konsultasi'),
]