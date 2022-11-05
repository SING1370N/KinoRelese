from celery import shared_task

from django.core.mail import send_mail

from time import sleep

import adminLte.models
from KinoCMS.settings import EMAIL_HOST_USER


@shared_task
def stat(request):
    # db = adminLte.models.Statistic.objects.get(id=1)
    # if str(request.META['HTTP_USER_AGENT']).count('Windows') > 0:
    #     db.windows += 1
    #     db.save()
    # elif str(request.META['HTTP_USER_AGENT']).count('Linux') > 0:
    #     db.linux += 1
    #     db.save()
    # else:
    #     db.os += 1
    #     db.save()
    return None


@shared_task
def send_tg(message):
    import telebot
    bot = telebot.TeleBot('5119945941:AAGqsBh-QieLmkLNliy8wI2EJCqtGSPomxw')
    sleep(5)
    bot.send_message(242284032, f"{message}")
    return None


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_email_task(title: str, text: str, recipient: list, email: str = EMAIL_HOST_USER):
    sleep(10)
    send_mail(title,
              text,
              email,
              recipient)
    return None
