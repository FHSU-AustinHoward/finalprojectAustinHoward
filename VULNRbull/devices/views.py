from django.http import HttpResponse

from .nvdlib_handler import Device, debug_info as nvd_debug_info

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Device

@login_required
def index(request):
    if request.method == 'POST':
        # Get the device name from the form data
        device_name = request.POST.get('device_name')
        if device_name:
            # Create a new Device object using the model method
            new_device = Device()
            new_device.create_from_api(request.user.username, device_name)
            # Redirect to the same page (refresh) after adding the device
            return redirect('index')

    # If it's a GET request or if the form submission failed, retrieve the existing devices
    devices = Device.objects.filter(username=request.user.username)
    context = {'devices': devices} if devices.exists() else {}
    return render(request, 'devices/index.html', context)


def detail(request, device_id):
    return HttpResponse("You're looking at device %s." % device_id)
