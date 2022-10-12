from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from cinema.models import Film, Cinema
from pages.models import News_promo, Page
from baners.models import Banner_news, Banner


# Create your views here.
def index(request):
    # print(range(Banner.objects.count()))
    return render(request, 'main/index.html', {"pages": Page.objects.all(), "banners_num": range(Banner.objects.count()), "banners_logo": Banner.objects.all(), "films": Film.objects.all()})


def news(request):
    return render(request, 'main/news.html', {"pages": Page.objects.all(),"news_all": News_promo.objects.all()})


def cinema(request):
    return render(request, 'main/cinema.html', {"pages": Page.objects.all(),"cinema": Cinema.objects.all()})


def about(request):
    return render(request, 'main/about.html', {"pages": Page.objects.all()})


def other_page(request, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))
