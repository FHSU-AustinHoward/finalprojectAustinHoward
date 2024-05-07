from django.db import models

# Create your models here.
class Vulnerability(models.Model):
    cve_id = models.CharField(max_length=100)
    cve_descriptions = models.TextField()
    cve_score = models.FloatField()
    cve_url = models.URLField()

    def __str__(self):
        return self.cve_id

class Software(models.Model):
    name = models.CharField(max_length=100)
    vulnerabilities = models.ManyToManyField(Vulnerability)

    def __str__(self):
        return self.name

class Device(models.Model):
    username = models.CharField(max_length=100)
    device_name = models.CharField(max_length=100)
    os_name = models.CharField(max_length=100)
    software = models.ManyToManyField(Software)

    def __str__(self):
        return self.device_name
