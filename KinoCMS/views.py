# from django.http import HttpResponse
# from django_faker import Faker
from django.shortcuts import redirect

# from cinema.models import Film
# from users.forms import CustomUserCreationForm
# from django.core.mail import send_mail
# from sendg.views import send_tg
from sendg.views import send
from sendg.tasks import send_tg


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def test(request):
    title = "Information"
    text = "This is text"
    to = ['djoddy83@gmail.com']
    # send_tg.delay(f"{title}, {text}, {', '.join(to)}, {get_client_ip(request)}")
    send(title, text, to)
    return redirect('statistic')
#     test = Faker.getPopulator()
#     test.addEntity(CustomUserCreationForm, 5)
#     insertedPks = test.execute()
#     return render(request, 'index.html')
