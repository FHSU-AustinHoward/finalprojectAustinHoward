from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the devices index.")


def detail(request, device_id):
    return HttpResponse("You're looking at device %s." % device_id)
