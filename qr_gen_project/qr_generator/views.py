# account/views.py

from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'qr_generator/index.html', context)