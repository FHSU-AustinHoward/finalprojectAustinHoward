from django.http import HttpResponse

from .models import Device
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    devices = Device.objects.filter(username=request.user.username)
    context = {'devices': devices} if devices.exists() else {}
    return render(request, 'devices/index.html', context)


def detail(request, device_id):
    return HttpResponse("You're looking at device %s." % device_id)
