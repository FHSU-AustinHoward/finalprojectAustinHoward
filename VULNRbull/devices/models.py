from django.db import models
from .nvdlib_handler import (Device as handler_device,
                             debug_info as debug)


class Vulnerability(models.Model):
    cve_id = models.CharField(max_length=100)
    cve_score = models.FloatField()
    cve_url = models.URLField()

    def __str__(self):
        return self.cve_id

    class Meta:
        verbose_name_plural = "Vulnerabilities"


class Software(models.Model):
    name = models.CharField(max_length=100)
    cpe_name = models.CharField(max_length=255, default='CPE Unknown')
    vulnerabilities = models.ManyToManyField(Vulnerability)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Software"


class Device(models.Model):
    username = models.CharField(max_length=100)
    device_name = models.CharField(max_length=100)
    os_name = models.CharField(max_length=100)
    software = models.ManyToManyField(Software)

    def create_from_api(self, username, device_name):
        pass

    def __str__(self):
        return self.device_name
