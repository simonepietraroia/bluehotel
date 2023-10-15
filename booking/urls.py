from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home_page, name= 'get_home_page'),
    path('create/', views.GuestBookingView, name='create_booking')
]