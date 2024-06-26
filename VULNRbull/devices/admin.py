# INF601 - Advanced Programming in Python
# Austin Howard
# Final Project

from django.contrib import admin
from .models import Device, Software, Vulnerability


from django.contrib import admin
from .models import Vulnerability, Software, Device


class VulnerabilityAdmin(admin.ModelAdmin):
    list_display = ('cve_id', 'cve_score', 'date_created', 'cve_url')
    list_filter = ["date_created", "cve_score"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # Sort queryset by cve_score in descending order
        return queryset.order_by('-cve_score')

class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpe_name', 'date_created')
    list_filter = ["date_created"]

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('username', 'device_name', 'os_name', 'software_found', 'vulnerabilities_found', 'date_created')
    list_filter = ["date_created", "username"]


admin.site.register(Vulnerability, VulnerabilityAdmin)
admin.site.register(Software, SoftwareAdmin)
admin.site.register(Device, DeviceAdmin)
