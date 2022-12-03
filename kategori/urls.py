from django.urls import path

from .views import index, add_kategori

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_kategori, name='add_kategori'),
]