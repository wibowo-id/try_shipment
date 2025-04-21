from django.shortcuts import render, redirect, get_object_or_404
from .models import EkspedisiPengiriman, TrackingPengiriman, LayananPengiriman
from django.utils import timezone

# Create your views here.
# Tampilkan semua layanan
def list_layanan(request):
    layanan_list = LayananPengiriman.objects.all()
    return render(request, 'pengiriman/layanan/list.html', {'layanan_list': layanan_list})

# Tambah layanan baru
def tambah_layanan(request):
    if request.method == 'POST':
        nama = request.POST['nama_layanan']
        ongkos = request.POST['ongkos_kirim']
        LayananPengiriman.objects.create(nama_layanan=nama, ongkos_kirim=ongkos)
        return redirect('list_layanan')
    return render(request, 'pengiriman/layanan/tambah.html')

# Edit layanan
def edit_layanan(request, pk):
    layanan = get_object_or_404(LayananPengiriman, pk=pk)
    if request.method == 'POST':
        layanan.nama_layanan = request.POST['nama_layanan']
        layanan.ongkos_kirim = request.POST['ongkos_kirim']
        layanan.save()
        return redirect('list_layanan')
    return render(request, 'pengiriman/layanan/edit.html', {'layanan': layanan})

# Hapus layanan
def hapus_layanan(request, pk):
    layanan = get_object_or_404(LayananPengiriman, pk=pk)
    layanan.delete()
    return redirect('list_layanan')

def daftar_pengiriman(request):
    pengiriman = EkspedisiPengiriman.objects.all()
    return render(request, 'pengiriman/daftar.html', {'pengiriman': pengiriman})

def tambah_pengiriman(request):
    layanan_list = LayananPengiriman.objects.all()

    if request.method == 'POST':
        layanan_obj = LayananPengiriman.objects.get(id=request.POST['layanan'])

        EkspedisiPengiriman.objects.create(
            kode_resi=request.POST['kode_resi'],
            pengirim_nama=request.POST['pengirim_nama'],
            penerima_nama=request.POST['penerima_nama'],
            kota_asal=request.POST['kota_asal'],
            kota_tujuan=request.POST['kota_tujuan'],
            berat_kg=request.POST['berat_kg'],
            layanan=layanan_obj,
        )
        return redirect('daftar_pengiriman')
    return render(request, 'pengiriman/tambah.html', {'layanan_list': layanan_list})

def update_status(request, resi):
    pengiriman = get_object_or_404(EkspedisiPengiriman, kode_resi=resi)
    if request.method == 'POST':
        status = request.POST['status']
        lokasi = request.POST['lokasi']
        pengiriman.status_pengiriman = status
        pengiriman.save()

        TrackingPengiriman.objects.create(
            pengiriman=pengiriman,
            status=status,
            lokasi=lokasi,
            waktu_update=timezone.now()
        )
        return redirect('daftar_pengiriman')
    return render(request, 'pengiriman/update.html', {'pengiriman': pengiriman})

def tracking_detail(request, resi):
    pengiriman = get_object_or_404(EkspedisiPengiriman, kode_resi=resi)
    tracking = TrackingPengiriman.objects.filter(pengiriman=pengiriman).order_by('waktu_update')
    return render(request, 'pengiriman/tracking.html', {'pengiriman': pengiriman, 'tracking': tracking})