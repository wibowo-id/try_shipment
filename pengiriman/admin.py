from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import EkspedisiPengiriman, TrackingPengiriman, LayananPengiriman

admin.site.register(EkspedisiPengiriman)
admin.site.register(TrackingPengiriman)
admin.site.register(LayananPengiriman)