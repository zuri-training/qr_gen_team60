# account/views.py
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

from django.contrib.auth import get_user_model

User = get_user_model()
# --------------------imports

from django.shortcuts import render
from django.conf import settings
from qrcode import *
import time
from .models import QRCollection


def index(request):
    context = {}
    return render(request, 'qr_generator/index.html', context)


# def qr_gen(request):
#     if request.method == 'POST':
#         data = request.POST['data']
#         img = make(data)
#         img_name = 'qr' + str(time.time()) + '.png'
#         img.save(str(settings.MEDIA_ROOT) + '/' + img_name)
#         return render(request, 'generator.html', {'img_name': img_name})
#     return render(request, 'generator.html')
def category(request, pk):
    if pk == "image":
        return 'image'

def generate(request, *extra_args):
    context = {}

    if request.method == 'POST':
        
        if extra_args['image']:
            val = None
            match (extra_args[0]):
                case 'image':
                    val = 'image'

                case 'pdf':
                    val = 'file'

                case 'url':
                    val = 'url'

            context[val] = val

            return render(request, 'qr_generator/generator.html', context)
        else:
            link_to_logo = STATIC_ROOT + '/base/images/' + 'qr_logo.png'
            logo = Image.open(link_to_logo)
            
            basewidth = 100

            # adjust image size
            widthpercent = (basewidth/float(logo.size[0]))
            hsize = int((float(logo.size[1])*float(widthpercent)))

            logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
            QRcode = qrcode.QRCode(
                version=3,
                box_size = 10,
                border=2,
                error_correction=qrcode.constants.ERROR_CORRECT_M
            )

            data = request.POST['data']

            QRcode.make(fit=True)
            
            QRimg = QRcode.make_image(
                fill_color='black', back_color="white").convert('RGB')
            
            # set size of QR code
            pos = ((QRimg.size[0] - logo.size[0]) // 2,(QRimg.size[1] - logo.size[1]) // 2)

            QRimg.paste(logo, pos)

            img_name = '/upload/nick.png' # the folder must be pre-existing, time wasted to find out:6hrs
            QRimg.save(MEDIA_ROOT + img_name)
            
            loc = MEDIA_URL + img_name
            context['qr_image'] = loc

            return render(request, 'qr_generator/generator.html', context)
    
    else:
        return render(request, 'qr_generator/generator.html', context)

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


def qr_gen2(request):

    if request.method == "POST":
        # Take image for the QR type// will change to elizzy's idea later
        link_to_logo = STATIC_ROOT + '/images/' + 'qr_logo.png'
        logo = Image.open(link_to_logo)
        
        basewidth = 100

        # adjust image size
        widthpercent = (basewidth/float(logo.size[0]))
        hsize = int((float(logo.size[1])*float(widthpercent)))

        logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
        QRcode = qrcode.QRCode(
            version=3,
            box_size = 10,
            border=2,
            error_correction=qrcode.constants.ERROR_CORRECT_M
        )
        

        # take the user input
        # if the input is not text:
        #   collect the input,  
        #   get the location of the input with js
        #   send to the view
        #   sav
        input = request.POST.get('qr_value')
        QRcode.add_data(input)
        
        # generating QR code
        QRcode.make(fit=True)
        
        QRimg = QRcode.make_image(
            fill_color='black', back_color="white").convert('RGB')
        
        # set size of QR code
        pos = ((QRimg.size[0] - logo.size[0]) // 2,(QRimg.size[1] - logo.size[1]) // 2)

        QRimg.paste(logo, pos)
        
        # save the QR code generated
        QRimg.save(str(settings.MEDIA_ROOT) + '/' + str(request.user) + '2.png')
        qr = MEDIA_URL + str(request.user) + '2.png'

        
        print(f'QR code generated! it is at {qr}')
        return render(request, 'qr_generator/form.html', {"qr":qr})
    return render(request, 'qr_generator/form.html',)

    
def test_form(request, template):
    form = ContactUsForm()
    return render(request, "qr_generator/" + template +'.html',{"form":form})




def learn_more(request):
    return render(request, 'base/coming_soon.html')

# def qr_gen(request):
#     if request.method == 'POST':
#         data = request.POST['data']
#         img = make(data)
#         img_name = 'qr' + str(time.time()) + '.png'
#         img.save(str(settings.MEDIA_ROOT) + '/' + img_name)
#         return render(request, 'generator.html', {'img_name': img_name})
#     return render(request, 'qr_generator/generator.html')

def get_qr(request, qr_id):
    collection = QRCollection.objects.get(id=qr_id)
    return render(request, "", {"qr":collection})


def page_not_found(request, exception):
    return render(request, 'base/error404.html', status=404)