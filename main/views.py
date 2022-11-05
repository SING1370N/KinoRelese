from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template

from adminLte.models import Statistic
from cinema.models import Film, Cinema, Session
from pages.models import News_promo, Page
from baners.models import Banner_news, Banner
from main.tasks import sendsss


# Create your views here.
def index(request):
    # sendsss("Hi")
    # print(range(Banner.objects.count()))
    db = Statistic.objects.get(id=1)
    if str(request.META['HTTP_USER_AGENT']).count('Windows') > 0:
        db.windows += 1
    elif str(request.META['HTTP_USER_AGENT']).count('Linux') > 0:
        db.linux += 1
    else:
        db.os += 1
    if str(request.META['HTTP_USER_AGENT']).count('Firefox/') > 0:
        db.firefox += 1
    elif str(request.META['HTTP_USER_AGENT']).count('Chrome/') > 0:
        db.chrome += 1
    elif str(request.META['HTTP_USER_AGENT']).count('Opera/') > 0:
        db.opera += 1
    elif str(request.META['HTTP_USER_AGENT']).count('Safari/') > 0:
        db.safari += 1
    else:
        db.browser += 1
    db.save()
    return render(request, 'main/index.html',
                  {"pages": Page.objects.all(), "banners_num": range(Banner.objects.count()),
                   "banners_logo": Banner.objects.all(), "films": Film.objects.all()})


def schedule(request):
    return render(request, 'main/schedule.html', {"pages": Page.objects.all(), "films": Session.objects.all()})
def news(request):
    return render(request, 'main/news.html', {"pages": Page.objects.all(), "news_all": News_promo.objects.all()})


def cinema(request):
    return render(request, 'main/cinema.html', {"pages": Page.objects.all(), "cinema": Cinema.objects.all()})


def about(request):
    return render(request, 'main/about.html', {"pages": Page.objects.all()})


def other_page(request, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))
