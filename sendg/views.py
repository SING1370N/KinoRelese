from django.shortcuts import render
from django.core.mail import send_mail

# селери
# Create your views here.
def send(title, text, to: list):
    send_mail(title, text, None, to, fail_silently=False,)
