from django.urls import path
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    path('', views.play, name='picsna-home'),
    path('play/', views.play, name='picsna-play'),
    path('addImg/', views.addImg, name='picsna-addImg'),

    path('../users/register/', user_views.register, name='users-register'),
    path('../users/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='users-login'),
    path('../users/logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='users-logout'),
    
]