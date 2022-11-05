import time

from celery import Celery

# app = Celery('tasks', broker='amqp://localhost')
from celery import shared_task

@shared_task
def add(x, y):
    return x + y

@shared_task
def sendsss(message):
    import telebot

    ADMIN = 242284032
    API_TOKEN = '5119945941:AAGqsBh-QieLmkLNliy8wI2EJCqtGSPomxw'
    bot = telebot.TeleBot(API_TOKEN)
    for i in range(15):
        print(i)
        time.sleep(5)
    bot.send_message(ADMIN, f"{message}")

    # def send_tg(message):
    #     #
    #     pass

