"""tubethemes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from core.views import IndexTubeListView, UserCreateView, ThemeCreateView, TubeCreateView
from core.views import UpTubeAjaxView, DownTubeAjaxView, ThemeListView
from core.forms import LoginForm

urlpatterns = [
    path('', IndexTubeListView.as_view(), name='index'),
    path('themes', ThemeListView.as_view(), name='themes'),
    path('new-theme', ThemeCreateView.as_view(), name='new_theme'),
    path('new-tube', TubeCreateView.as_view(), name='new_tube'),
    path('up-tube/', UpTubeAjaxView.as_view(), name='up_tube'),
    path('down-tube/', DownTubeAjaxView.as_view(), name='down_tube'),
    path('admin/', admin.site.urls),
    path('accounts/login/',LoginView.as_view(authentication_form=LoginForm), name='login'),
    path('register',UserCreateView.as_view(), name='register'),
    path('quit',LogoutView.as_view(), name='logout')
]
