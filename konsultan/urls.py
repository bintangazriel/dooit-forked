from django.urls import path
from .views import dashboard_konsultan, profil_konsultan

urlpatterns = [
    path('dashboard/', dashboard_konsultan, name='dashboard_konsultan'),
    path('profile/', profil_konsultan, name='profil_konsultan'),
]