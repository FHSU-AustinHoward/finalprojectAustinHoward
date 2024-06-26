# INF601 - Advanced Programming in Python
# Austin Howard
# Final Project

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Device

@login_required
def index(request):
    # Process POST request to add a new device
    if request.method == 'POST':
        device_name = request.POST.get('device_name')
        if device_name:
            # Fetch device information and redirect to index
            Device.fetch_device_info(request.user.username, device_name)
            return redirect('index')

    # Retrieve devices associated with the logged-in user
    devices = Device.objects.filter(username=request.user.username).order_by('-date_created')
    context = {'devices': devices} if devices.exists() else {}
    return render(request, 'devices/index.html', context)


@login_required
def detail(request, device_id):
    # Retrieve the details of a specific device
    device = get_object_or_404(Device, pk=device_id)
    return render(request, 'devices/detail.html', {'device': device})
