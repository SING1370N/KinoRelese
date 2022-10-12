from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cinema.models import Film, Cinema
from baners.models import Banner_news, Banner


# Create your views here.
@login_required(login_url='Login')
def statistic(request):
    return render(request, 'adminLte/statistic.html',
                  {"banners_num": range(Banner.objects.count()), "posts": Banner.objects.all(),
                   "films": Film.objects.all()})
    # context = {}
    # return render(request, 'adminLte/statistic.html', context)


@login_required(login_url='Login')
def banners_page(request):
    context = {}
    return render(request, 'adminLte/banners.html', context)
