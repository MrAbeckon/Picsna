from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.play, name='picsna-home'),
    path('play/', views.play, name='picsna-play'),
]