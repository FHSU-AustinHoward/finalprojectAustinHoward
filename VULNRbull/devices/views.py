from django.http import HttpResponse

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Device

@login_required
def index(request):
    if request.method == 'POST':
        device_name = request.POST.get('device_name')
        if device_name:
            new_device = Device.fetch_device_info(request.user.username, device_name)
            return redirect('index')

    devices = Device.objects.filter(username=request.user.username).order_by('-date_created')  # Sort devices by most recent date_created
    context = {'devices': devices} if devices.exists() else {}
    return render(request, 'devices/index.html', context)


def detail(request, device_id):
    device = get_object_or_404(Device, pk=device_id)
    return render(request, 'devices/detail.html', {'device': device})