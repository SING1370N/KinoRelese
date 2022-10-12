"""KinoCMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import KinoCMS.views
from pages.views import page
from main.views import index
from users.views import login_page, create_user, logout_user
from django.conf.urls.static import static
from django.conf import settings


#     path('login/', login_page, name='login_page'),
#     path('update/<int:user_id>', update_user, name='update_user'),
#     path('register/', create_user, name='register'),
#     path('logout/', logout_user, name='logout'),
#     path('users/', users, name='users'),

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('database/', admin.site.urls),
    path('test/', KinoCMS.views.test, name='test'),

    path('main/', index, name='main'),
    path('page/<int:page_id>', page, name='page'),

    path('login/', login_page, name='Login'),
    path('register/', create_user, name='Register'),
    path('logout/', logout_user, name='logout'),

    path('adminlte/', include('adminLte.urls'), name='admin'),

    path('', include('main.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
