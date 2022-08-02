# account/views.py

from django.shortcuts import render
from django.conf import settings
from qrcode import *
import time
from .models import QRCollection

def index(request):
    context = {}
    return render(request, 'qr_generator/generator.html', context)


def qr_gen(request):
    if request.method == 'POST':
        data = request.POST['data']
        img = make(data)
        img_name = 'qr' + str(time.time()) + '.png'
        img.save(str(settings.MEDIA_ROOT) + '/' + img_name)
        return render(request, 'generator.html', {'img_name': img_name})
    return render(request, 'generator.html')

def get_qr(request, qr_id):
    collection = QRCollection.objects.get(id=qr_id)
    return render(request, "", {"qr":collection})


# QRCollection.objects.create()