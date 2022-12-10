from django.urls import path
from .views import dashboard_konsultan

app_name = 'konsultan'

urlpatterns = [
    path('dashboard/', dashboard_konsultan, name='dashboard_konsultan'),
]