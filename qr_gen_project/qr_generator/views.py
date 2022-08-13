# account/views.py
import base64
from smtplib import SMTPServerDisconnected
from django.http import BadHeaderError, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.conf import settings

from django.core.mail import send_mail
from django.contrib import messages

from qr_generator.forms import ContactUsForm 
import qrcode
from PIL import Image
from django.conf import settings
from qr_gen_project.settings import MEDIA_URL, STATIC_ROOT, STATIC_URL, MEDIA_ROOT
import datetime
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model

# --------------------imports

from django.shortcuts import render
from django.conf import settings
from qrcode import *
from .models import QRCollection


import mimetypes
import os
from django.http.response import HttpResponse
from qr_generator.models import Category
from django.core.files import File

User = get_user_model()


OUR_LOGO = STATIC_ROOT + '/base/images/' + 'qr_logo.png'


def index(request):
    context = {}
    return render(request, 'qr_generator/index.html', context)


def get_current_time():
    now = str(datetime.datetime.now()).split('.')
    return str(now[1])


def share_qr(request, pk):
    return render(request, 'qr_generator/share_qr.html', {'qr_image':pk})

def save_qr(request, ):
    pass


# Convert to JPEG
def convert_to_jpeg(path):
    image = Image.open(path)
    rgb_image = image.convert('RGB')
    jpeg_image = rgb_image.save(path.replace('.png', '.jpeg'), 'JPEG')
    return path.replace('.png', '.jpeg'), os.path.basename(path.replace('.png', '.jpeg'))

def convert_to_png(path):
    image = Image.open(path)
    rgb_image = image.convert('RGB')
    png_image = rgb_image.save(path.replace('.png', '.png'), 'PNG')
    return path.replace('.png', '.png'), os.path.basename(path.replace('.png', '.png'))

# Convert to JPG
def convert_to_jpg(path):
    image = Image.open(path)
    rgb_image = image.convert('RGB')
    jpg_image = rgb_image.save(path.replace('.png', '.jpg'), 'JPG')
    return path.replace('.png', '.jpg'), os.path.basename(path.replace('.png', '.jpg'))


# Convert to SVG
def convert_to_svg(path):
    startSvgTag = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
    "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
    <svg version="1.1"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    width="240px" height="240px" viewBox="0 0 240 240">"""
    endSvgTag = """</svg>"""
    pngFile = open(path, 'rb')
    base64data = base64.b64encode(pngFile.read())
    base64String = '<image xlink:href="data:image/png;base64,{0}" width="240" height="240" x="0" y="0" />'.format(base64data.decode('utf-8'))
    f = open(path.replace('.png', '.svg'), 'w')
    f.write(startSvgTag + base64String + endSvgTag)
    f.close()
    return path.replace('.png', '.svg'), os.path.basename(path.replace('.png', '.svg'))


# Convert to PDF
def convert_to_pdf(path):
    image = Image.open(path)
    rgb_image = image.convert('RGB')
    pdf_image = rgb_image.save(path.replace('.png', '.pdf'), 'PDF')
    return path.replace('.png', '.pdf'), os.path.basename(path.replace('.png', '.pdf'))



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

        QRimg.paste(our_logo, pos) # save to db here

        img_name = '/upload/' + str(request.user.username) +  now + '.png' # the folder must be pre-existing, time wasted to find out:6hrs

        # file_name = '{0}_{1}.png'.format(request.user.username, now)

        QRimg.save(MEDIA_ROOT + img_name)
        QRCollection.objects.create(
            qr_user = request.user,
            category = 'QRCode',
            qr_code = File(QRimg),
            qr_name = str(request.user.username) + '\'s Qr'
            )
        
        loc = MEDIA_URL + img_name
        context['qr_image'] = loc
        print(loc)

    return render(request, template, context)


def category(request, pk):
    if pk == "image":
        return 'image'

def save_qr(request):
    print(request.user)
    print('Save clicked')

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
            reciever = settings.EMAIL_HOST_USER

            try:
                send_mail(subject, message, from_email, [reciever,])
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
        form = ContactUsForm()

    context['form'] = form
    
    return render(request, 'qr_generator/contact.html', context)




# Define function to download pdf file using template
def download_file(request, filetype=''):


    if filetype != '':

        obj = request.post['img']
        
        if filetype == 'pdf':
            print("\n\nPDF selected\n\n")
            filepath, filename = convert_to_pdf(obj)
        
        elif filename == 'png':
            filepath, filename = convert_to_png(obj)
        
        elif filename == 'jpg':
            filepath, filename = convert_to_jpg(obj)
        
        elif filename == 'svg':
            filepath, filename = convert_to_svg(obj)
        
        elif filename == 'jpeg':
            filepath, filename = convert_to_jpeg(obj)
        
        

        path = open(filepath, 'rb')
        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response





# def code_download_pdf(request, pk):
#     obj = get_object_or_404(QrCode.objects.filter(user=request.user), pk=pk)
#     filepath, filename = convert_to_pdf(obj.qr_code.path)
#     response = HttpResponse(open(filepath, 'rb').read(), content_type='application/force-download')
#     response['Content-Disposition'] = 'attachment; filename=%s' % filename
#     return response



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

