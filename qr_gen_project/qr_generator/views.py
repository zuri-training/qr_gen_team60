# account/views.py

from smtplib import SMTPServerDisconnected
from django.http import BadHeaderError, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.conf import settings
from qrcode import *
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

# --------------------imports



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




def form(request, template):
    form = ContactUsForm()
    return render(request, "qr_generator/" + template +'.html', {"form":form})


def contact_us(request):
    logger = logging.getLogger(__name__) # logger to  view errors
 
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
            except BadHeaderError:
                messages.error(request, message="Invalid Header")
                return HttpResponse('Invalid header found.')

            except SMTPServerDisconnected:
                messages.error(request, message="Network Connection failed")
                return redirect(to='qr_generator:contact')

            except Exception as err:
                logger.warning(f'{err} [{request.user}] tried Contacting us at '+str(datetime.datetime.now())+' hours! but couldn\'t')
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