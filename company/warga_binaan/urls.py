from django.urls import path
from . import views

urlpatterns = [
    path('', views.tabel_warga_binaan, name='warga_binaan'),
]