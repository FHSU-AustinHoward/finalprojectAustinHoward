# INF601 - Advanced Programming in Python
# Austin Howard
# Final Project

import os
import platform

from django.db import models
from .nvdlib_handler import search_cpe_by_name, search_cves_by_cpe, search_installed_software, debug_info
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
DEBUGGING = os.getenv("NVDLIB_DEBUGGING")



class Vulnerability(models.Model):
    # Attributes
    cve_id = models.CharField(max_length=100)
    cve_score = models.FloatField()
    cve_url = models.URLField()
    linked_software = models.ManyToManyField('Software')  # Link vulnerabilities to software instances
    linked_device = models.ManyToManyField('Device')
    date_created = models.DateTimeField(auto_now_add=True)  # Add date created field

    def __str__(self):
        return self.cve_id

    class Meta:
        # Fixes the display on the admin page
        verbose_name_plural = "Vulnerabilities"


class Software(models.Model):
    # Attributes
    name = models.CharField(max_length=100)
    cpe_name = models.CharField(max_length=255, default='CPE Unknown')
    vulnerabilities = models.ManyToManyField(Vulnerability)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        # Fixes the display on the admin page
        verbose_name_plural = "Software"

    @classmethod
    def fetch_software(cls, software_name):
        """
        Fetches software information based on the software name.
        """
        cpe_name = search_cpe_by_name(software_name)
        if cpe_name:
            # Check if software with this name already exists
            software, created = cls.objects.get_or_create(
                name=software_name,
                defaults={'cpe_name': cpe_name}
            )
            # If the software already exists, update its vulnerabilities
            if not created:
                vulnerabilities = search_cves_by_cpe(cpe_name)
                software.vulnerabilities.clear()  # Clear existing vulnerabilities
                for v in vulnerabilities:
                    vulnerability, _ = Vulnerability.objects.get_or_create(
                        cve_id=v.id,
                        defaults={
                            'cve_score': v.score[1],
                            'cve_url': v.url
                        }
                    )
                    # Add new vulnerability
                    software.vulnerabilities.add(vulnerability)
            else:
                # Otherwise, find the vulnerabilities
                vulnerabilities = search_cves_by_cpe(cpe_name)
                for v in vulnerabilities:
                    vulnerability, _ = Vulnerability.objects.get_or_create(
                        cve_id=v.id,
                        defaults={
                            'cve_score': v.score[1],
                            'cve_url': v.url
                        }
                    )
                    # Add vulnerability to newly created software
                    software.vulnerabilities.add(vulnerability)
            return software
        else:
            return None


class Device(models.Model):
    # Attributes
    username = models.CharField(max_length=100)
    device_name = models.CharField(max_length=100)
    os_name = models.CharField(max_length=100)
    software = models.ManyToManyField(Software)
    software_found = models.IntegerField(default=0)
    vulnerabilities_found = models.IntegerField(default=0)
    vulnerabilities = models.ManyToManyField(Vulnerability)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.device_name

    @classmethod
    def fetch_device_info(cls, username, device_name):
        """
        Fetches device information including software details.
        """

        # Fetch device operating system
        os_name = platform.platform()
        debug_info(username, device_name)

        # Fetch installed software and associated vulnerabilities
        installed_software = search_installed_software()
        software_instances = []
        vulnerabilities = []
        for software_name in installed_software:
            software = Software.fetch_software(software_name)
            if software:
                software_instances.append(software)
                vulnerabilities.extend(software.vulnerabilities.all())

        # Update software_found and vulnerabilities_found
        software_count = len(software_instances)
        vulnerabilities_count = len(vulnerabilities)

        # Create or fetch the device instance
        device, created = cls.objects.get_or_create(
            username=username,
            device_name=device_name,
            os_name=os_name,
        )
        device.software.add(*software_instances)
        vulnerabilities_set = set(vulnerabilities)
        device.vulnerabilities.set(vulnerabilities_set)

        # Update counts
        device.software_found = software_count
        device.vulnerabilities_found = vulnerabilities_count
        device.save()

        return device
