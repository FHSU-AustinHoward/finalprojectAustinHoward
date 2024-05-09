# INF601 - Advanced Programming in Python
# Austin Howard
# Final Project

from django.apps import AppConfig


class DevicesConfig(AppConfig):
    # Configures the Device app for VULNRbull
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'devices'
