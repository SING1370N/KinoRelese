from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from adminLte.models import Statistic
from sendg.views import send
from .models import User
from .forms import CustomUserChangeForm, CustomUserCreationForm
def login_page(request):
    if request.user.is_authenticated:
        return redirect('admin')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # url_from = request.META['HTTP_REFERER']
        # print(request.POST.get('next'))
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # send(request.META['HTTP_USER_AGENT'])
            # print(request.META['HTTP_USER_AGENT'])
            login(request, user)
            # url_from = request.META['HTTP_REFERER']
            return redirect('admin')
            # return redirect('statistic')
        else:
            messages.info(request, 'Щось не так, спробуйте ще')
    context = {}
    return render(request, 'users/login.html', context)


@login_required(login_url='Login')
def update_user(request, user_id):
    obj_user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance=obj_user)
        if user_change_form.is_valid():
            user = user_change_form.save(commit=False)

            password1 = request.POST.get('password1')
            if password1 != "":
                # user.password = make_password("1111")
                user.set_password(password1)
                # user.save()
            user.save()
            return redirect('users')
    else:
        user_change_form = CustomUserChangeForm(instance=obj_user)

    context = {'user_form': user_change_form}
    return render(request, 'users/user_update.html', context)


def create_user(request):
    if request.user.is_authenticated:
        return redirect('admin')
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(request.POST)
        if user_creation_form.is_valid():
            user = user_creation_form.save(commit=False)
            user.save()
            messages.success(request, 'User' + user.username + 'create successful')
            return redirect('Login')
    else:
        user_creation_form = CustomUserCreationForm()

    context = {'user_form': user_creation_form}
    return render(request, 'users/register.html', context)


@login_required(login_url='Login')
def logout_user(request):
    logout(request)
    return redirect('Login')

@login_required(login_url='Login')
def users(request):
    obj_users = User.objects.all()
    context = {'users': obj_users}
    return render(request, 'users/users.html', context)


def password(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'POST':
        username = request.POST.get('username')
        mail = request.POST.get('email')
        obj_users = User.objects.all()
        for name in obj_users:
            if str(name) == username:
                if str(name.email) == mail:
                    from django.contrib.auth.hashers import make_password
                    print(name.password)
                    name.password = make_password("1111")
                    name.set_password("1111")
                    name.save()
                    print(name.password)
                    messages.success(request,
                                     f"sha1 це хеш, він не має нового паролю, але створенний новий пароль для {username} - 1111")
                else:
                    messages.success(request,
                                     f"Sorry, no")

    context = {}
    return render(request, 'users/password.html', context)
