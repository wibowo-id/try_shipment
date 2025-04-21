import math
from django.db import models

# Create your models here.
class LayananPengiriman(models.Model):
    nama_layanan = models.CharField(max_length=50)
    ongkos_kirim = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.nama_layanan} (Rp{self.ongkos_kirim})"

class EkspedisiPengiriman(models.Model):
    kode_resi = models.CharField(max_length=50, unique=True)
    pengirim_nama = models.CharField(max_length=100)
    penerima_nama = models.CharField(max_length=100)
    kota_asal = models.CharField(max_length=100)
    kota_tujuan = models.CharField(max_length=100)
    berat_kg = models.DecimalField(max_digits=10, decimal_places=2)
    layanan = models.ForeignKey(LayananPengiriman, on_delete=models.CASCADE)
    status_pengiriman = models.CharField(max_length=50, default='diproses')
    tanggal_kirim = models.DateTimeField(auto_now_add=True)
    total_biaya = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.kode_resi
    
    def save(self, *args, **kwargs):
        if self.layanan and self.layanan.ongkos_kirim:
            berat = float(self.berat_kg)
            berat_dibulatkan = math.ceil(berat) if berat > 0.3 else 1
            self.total_biaya = berat_dibulatkan * float(self.layanan.ongkos_kirim)
        super().save(*args, **kwargs)

class TrackingPengiriman(models.Model):
    pengiriman = models.ForeignKey(EkspedisiPengiriman, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    lokasi = models.CharField(max_length=100)
    waktu_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pengiriman.kode_resi} - {self.status}"