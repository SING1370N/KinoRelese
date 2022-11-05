from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Statistic(models.Model):
    firefox = models.IntegerField(default=0)
    chrome = models.IntegerField(default=0)
    safari = models.IntegerField(default=0)
    ie = models.IntegerField(default=0)
    opera = models.IntegerField(default=0)
    browser = models.IntegerField(default=0)

    linux = models.IntegerField(default=0)
    windows = models.IntegerField(default=0)
    os = models.IntegerField(default=0)
