# Generated by Django 5.2 on 2025-04-21 14:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EkspedisiPengiriman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_resi', models.CharField(max_length=50, unique=True)),
                ('pengirim_nama', models.CharField(max_length=100)),
                ('penerima_nama', models.CharField(max_length=100)),
                ('kota_asal', models.CharField(max_length=100)),
                ('kota_tujuan', models.CharField(max_length=100)),
                ('berat_kg', models.DecimalField(decimal_places=2, max_digits=10)),
                ('layanan', models.CharField(max_length=50)),
                ('status_pengiriman', models.CharField(default='diproses', max_length=50)),
                ('tanggal_kirim', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrackingPengiriman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
                ('lokasi', models.CharField(max_length=100)),
                ('waktu_update', models.DateTimeField(auto_now_add=True)),
                ('pengiriman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pengiriman.ekspedisipengiriman')),
            ],
        ),
    ]
