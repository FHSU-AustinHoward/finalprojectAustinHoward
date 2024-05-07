import os
import platform

from django.db import models
from .nvdlib_handler import search_cpe_by_name, search_cves_by_cpe, search_installed_software, debug_info
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
DEBUGGING = os.getenv("NVDLIB_DEBUGGING", "False").lower() == "true"



class Vulnerability(models.Model):
    cve_id = models.CharField(max_length=100)
    cve_score = models.FloatField()
    cve_url = models.URLField()

    def __str__(self):
        return self.cve_id

    class Meta:
        verbose_name_plural = "Vulnerabilities"

    @classmethod
    def fetch_vulnerabilities(cls, cpe_name):
        """
        Fetches vulnerabilities associated with a given Common Platform Enumeration (CPE) name.
        """
        cve_entries = search_cves_by_cpe(cpe_name)
        vulnerabilities = []
        for cve_entry in cve_entries:
            vulnerability, created = cls.objects.get_or_create(
                cve_id=cve_entry.id,
                defaults={
                    'cve_score': cve_entry.score[1],
                    'cve_url': cve_entry.url
                }
            )
            vulnerabilities.append(vulnerability)
        return vulnerabilities

class Software(models.Model):
    name = models.CharField(max_length=100)
    cpe_name = models.CharField(max_length=255, default='CPE Unknown')
    vulnerabilities = models.ManyToManyField(Vulnerability)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Software"

    @classmethod
    def fetch_software(cls, software_name):
        """
        Fetches software information based on the software name.
        """
        cpe_name = search_cpe_by_name(software_name)
        if cpe_name:
            vulnerabilities = Vulnerability.fetch_vulnerabilities(cpe_name)
            software, created = cls.objects.get_or_create(
                name=software_name,
                defaults={'cpe_name': cpe_name}
            )
            software.vulnerabilities.add(*vulnerabilities)
            return software
        else:
            return None

class Device(models.Model):
    username = models.CharField(max_length=100)
    device_name = models.CharField(max_length=100)
    os_name = models.CharField(max_length=100)
    software = models.ManyToManyField(Software)

    def __str__(self):
        return self.device_name

    @classmethod
    def fetch_device_info(cls, username, device_name):
        """
        Fetches device information including software details.
        """
        # Call debug_info if DEBUGGING is True
        if DEBUGGING:
            debug_info(username, device_name)

        # Fetch device operating system
        os_name = platform.platform()

        # Fetch installed software and associated vulnerabilities
        installed_software = search_installed_software()
        software_instances = []
        for software_name in installed_software:
            software = Software.fetch_software(software_name)
            if software:
                software_instances.append(software)

        # Create or fetch the device instance
        device, created = cls.objects.get_or_create(
            username=username,
            device_name=device_name,
            os_name=os_name
        )
        device.software.add(*software_instances)

        return device
