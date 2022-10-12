from django.urls import path, include
from cinema.views import films, add_film, film_update
from .views import statistic, banners_page
from users.views import users, update_user, password
from baners.views import baners


urlpatterns = [
    path('', statistic, name='admin'),
    path('statistic/', statistic, name='statistic'),
    path('bantest/', banners_page, name='bantest'),

    path('cinema/', include('cinema.urls')),
    # path('banners/', include('baners.urls')),
    path('banners/', baners, name='banners'),
    path('pages/', include('pages.urls')),
    # path('user/', include('users.urls')),
    path('users/', users, name='users'),
    path('update/<int:user_id>', update_user, name='update_user'),
    path('password/', password, name='password'),
    # path('logout/', logout_user, name='logout'),

    # Films
    path('films/', films, name='films'),
    path('films/add/', add_film, name='add_film'),
    path('films/edit/<int:film_id>/', film_update, name='film_update'),

]

