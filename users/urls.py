from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from picsna import views as picsnaViews
from django.contrib import admin

urlpatterns = [
	path('',views.register, name='register'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('../picsna/play/', picsnaViews.play, name='picsna-play'),
 ]