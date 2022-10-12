from django.urls import path
from .views import index, films, add_film, film_update, add_cinema, cinemas, cinema_update, add_hall, delete_hall,\
    hall_update

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', cinemas, name='cinemas'),

    # path('cinemas/', cinemas, name='cinemas'),
    path('addcinema/', add_cinema, name='add_cinema'),
    path('edit/<int:cinema_id>', cinema_update, name='cinema_update'),
    path('addhall/<int:cinema_id>', add_hall, name='add_hall'),
    path('updatehall/<int:cinema_id>/<int:hall_id>', hall_update, name='hall_update'),
    path('deletehall/<int:cinema_id>/<int:hall_id>', delete_hall, name='delete_hall')

]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
