from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Device

@login_required
def index(request):
    if request.method == 'POST':
        device_name = request.POST.get('device_name')
        if device_name:
            new_device = Device.fetch_device_info(request.user.username, device_name)
            new_device.debug_info(request.user.username, device_name)
            return redirect('index')

    devices = Device.objects.filter(username=request.user.username)
    context = {'devices': devices} if devices.exists() else {}
    return render(request, 'devices/index.html', context)


def detail(request, device_id):
    return HttpResponse("You're looking at device %s." % device_id)
