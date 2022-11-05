from django.shortcuts import render
from django.core.mail import send_mail

from sendg.tasks import send_tg, send_email_task


# from tasks import send_email_task, send_tg


# селери
# Create your views here.
def send(title: str = '', text: str = '', to=None):
    send_tg.delay(f'{title}: {text} - {to}')
    if to is None:
        to = ['djh20002@gmail.com']
    send_email_task.delay(title, text, to)
