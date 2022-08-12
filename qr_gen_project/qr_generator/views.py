# account/views.py
import base64
from smtplib import SMTPServerDisconnected
from django.http import BadHeaderError, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.conf import settings
# from qrcode import *
import time
from django.core.mail import send_mail
from requests import request
from django.contrib import messages
from qr_generator.forms import ContactUsForm 
import qrcode
from PIL import Image
from django.conf import settings
from qr_gen_project.settings import MEDIA_URL, STATIC_ROOT, STATIC_URL, MEDIA_ROOT
import logging
import datetime
from django.contrib.auth.decorators import login_required

import os

from django.contrib.auth import get_user_model

User = get_user_model()
# --------------------imports

from django.shortcuts import render
from django.conf import settings
from qrcode import *
import time
from .models import QRCollection


OUR_LOGO = STATIC_ROOT + '/base/images/' + 'qr_logo.png'


def index(request):
    context = {}
    return render(request, 'qr_generator/index.html', context)


def get_current_time():
    now = str(datetime.datetime.now()).split('.')
    return str(now[1])


def share_qr(request, pk):
    return render(request, 'qr_generator/share_qr.html', {'qr_image':pk})



@login_required(login_url="/qr-gen/accounts/login")
def generate_qr(request):
    context = {}
    template = 'qr_generator/generateqr.html'
    now = get_current_time()

    user_data = request.POST

    if request.method == 'POST':
        data = user_data['text']

    
        our_logo = Image.open(OUR_LOGO)
    
        # adjust image size
        widthpercent = (100/float(our_logo.size[0]))
        hsize = int((float(our_logo.size[1])*float(widthpercent)))
        our_logo = our_logo.resize((100, hsize), Image.ANTIALIAS)

        QRcode = qrcode.QRCode(
        version=3,
        box_size = 10,
        border=2,
        error_correction=qrcode.constants.ERROR_CORRECT_M
        )

        QRcode.make(fit=True)
    
        QRimg = QRcode.make_image(
            fill_color='black', back_color="white").convert('RGB')


         # set size of QR code
        pos = (
            (QRimg.size[0] - our_logo.size[0]) // 2,
            (QRimg.size[1] - our_logo.size[1]) // 2
            )

        QRimg.paste(our_logo, pos)

        img_name = '/upload/' + str(request.user) +  now + '.png' # the folder must be pre-existing, time wasted to find out:6hrs

        QRimg.save(MEDIA_ROOT + img_name)
        
        loc = MEDIA_URL + img_name
        context['qr_image'] = loc
        print(loc)

    return render(request, template, context)


def category(request, pk):
    if pk == "image":
        return 'image'


def form(request, template):
    form = ContactUsForm()
    return render(request, "qr_generator/" + template +'.html', {"form":form})


def contact_us(request):
 
    context = {}
    if request.method == "POST":
        form =  ContactUsForm(request.POST)
        if form.is_valid():
            from_email = settings.EMAIL_HOST_USER
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message'] #request.POST.get('message')

            try:
                send_mail(subject, message, from_email, ['simplenicky1@gmail.com'])
                messages.success(request, message="Message Successfully sent!!")
                return redirect('qr_generator:home')
            except BadHeaderError:
                messages.error(request, message="Invalid Header")
                return HttpResponse('Invalid header found.')

            except SMTPServerDisconnected:
                messages.error(request, message="Network Connection failed")
                return redirect(to='qr_generator:contact')

            except Exception as err:
                return HttpResponse("We haven't encountered this problem before") # TODO: will fix this when error page comes

            else:
                messages.success(request, message="Message Successfully sent!!")
                form = ContactUsForm()#! change later
                return redirect("qr_generator:contact")
                
    else:
        form = ContactUsForm()

    context['form'] = form
    
    return render(request, 'qr_generator/contact.html', context)

# Import mimetypes module
import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse
# Import render module
from django.shortcuts import render

# Define function to download pdf file using template
def download_file(request, pk, filename=''):
    if filename != '':
       
        # Define the full file path
        filepath = pk
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        return response
    else:

        return render(request, 'file.html')







def test_form(request, template):
    form = ContactUsForm()
    return render(request, "qr_generator/" + template +'.html',{"form":form})




def learn_more(request):
    return render(request, 'base/coming_soon.html')



def get_qr(request, qr_id):
    collection = QRCollection.objects.get(id=qr_id)
    return render(request, "", {"qr":collection})


def page_not_found(request, exception):
    return render(request, 'base/error404.html', status=404)

