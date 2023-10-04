from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from .models import Room, Booking
from django.contrib.auth.mixins import LoginRequiredMixin


def get_home_page(request):
    return render(request, '../templates/base.html')

class RoomListView(ListView):
    model = Room
    template_name = 'room_list.html'
    context_object_name = 'rooms'

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    template_name = 'booking_form.html'
    fields = ['room', 'check_in_date', 'check_out_date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BookingDetailView(LoginRequiredMixin, DetailView):
    model = Booking
    template_name = 'booking_detail.html'
