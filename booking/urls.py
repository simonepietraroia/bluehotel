from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home_page, name= 'get_home_page'),
    path('create/', views.create_guest_booking, name='create_booking')
]