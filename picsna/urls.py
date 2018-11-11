from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.register, name='picsna-home'),
    path('register/', views.register, name='picsna-register'),
    path('login/', views.login, name='picsna-login'),
    path('play/', views.play, name='picsna-play'),
]