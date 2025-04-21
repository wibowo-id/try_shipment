from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_pengiriman, name='daftar_pengiriman'),
    path('tambah/', views.tambah_pengiriman, name='tambah_pengiriman'),
    path('update/<str:resi>/', views.update_status, name='update_status'),
    path('tracking/<str:resi>/', views.tracking_detail, name='tracking_detail'),

    path('layanan/', views.list_layanan, name='list_layanan'),
    path('layanan/tambah/', views.tambah_layanan, name='tambah_layanan'),
    path('layanan/edit/<int:pk>/', views.edit_layanan, name='edit_layanan'),
    path('layanan/hapus/<int:pk>/', views.hapus_layanan, name='hapus_layanan'),
]