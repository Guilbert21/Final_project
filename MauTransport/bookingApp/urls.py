from django.contrib import admin
from django.urls import path
from . import views
# from google import views as view


urlpatterns = [
    path('booking/', views.booking_f, name='booking-page'),
    path('history/', views.history, name='history-page')
]