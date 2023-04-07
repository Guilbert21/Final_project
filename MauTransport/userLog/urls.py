from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # homepage
    path('', views.home, name='home-page'),

    # register
    path('register/', views.register, name='register-page'),

    # login
    path('login/', views.login, name='login-page'),

    # error
    path('error/', views.error, name='error-page'),

    #feedback
    path('home/', views.save_feedback, name='home'),
]
