from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cinema.models import Film, Cinema
from baners.models import Banner_news, Banner
from users.models import User
from adminLte.models import Statistic


# Create your views here.
@login_required(login_url='Login')
def statistic(request):
    return render(request, 'adminLte/statistic.html',
                  {"banners_num": range(Banner.objects.count()), "posts": Banner.objects.all(), "users": User.objects.count(),
                   "films": Film.objects.all(), 'stat': Statistic.objects.all()})
    # context = {}
    # return render(request, 'adminLte/statistic.html', context)


@login_required(login_url='Login')
def banners_page(request):
    context = {}
    return render(request, 'adminLte/banners.html', context)
