from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from .models import Room, Booking


def get_home_page(request):
    return render(request, '../templates/base.html')

class RoomListView(ListView):
    model = Room
    template_name = 'room_list.html'
    context_object_name = 'rooms'
