from django.contrib import admin
from .models import Device, Software, Vulnerability

# Register your models here.
admin.site.register(Device)
admin.site.register(Software)
admin.site.register(Vulnerability)