# from django.template.defaulttags import url
from django.urls import path
from .views import index, cinema, about, other_page, news, schedule
from django.views.generic import RedirectView

app_name = 'main'

urlpatterns = [
    # url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
    # path(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
    path('main/', index, name='main'),
    path('poste/', index, name='index'),
    path('schedule/', schedule, name='schedule'),
    path('soon/', index, name='index'),
    path('cinemas/', cinema, name='cinema'),
    path('promotions/', index, name='index'),
    path('info/', index, name='index'),
    path('news/', news, name='news'),
    path('ads/', index, name='index'),
    path('cafe/', index, name='new'),
    path('mobile/', index, name='other'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
    path('about/', about, name='about'),
]
