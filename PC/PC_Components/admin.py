from django.contrib import admin
from .models import RAM, CPU, VideoCards, Motherboard, SSD, CPUSocket, type_RAM, PowerUnit

admin.site.register(RAM)
admin.site.register(CPU)
admin.site.register(VideoCards)
admin.site.register(Motherboard)
admin.site.register(SSD)
admin.site.register(CPUSocket)
admin.site.register(type_RAM)
admin.site.register(PowerUnit)