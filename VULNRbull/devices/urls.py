from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # ex: /devices/5/
    path("<int:device_id>/", views.detail, name="detail"),
]