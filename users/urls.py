from django import urls
from django.urls import path
from . import views

urlpatterns  = [
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('singup', views.singup_view, name='singup'),
    path('profile', views.profile, name='profile'),
]