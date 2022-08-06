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
