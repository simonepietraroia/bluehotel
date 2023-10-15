from django.shortcuts import render, get_object_or_404, redirect
from .models import GuestBooking

def get_home_page(request):
    return render(request, '../templates/index.html')

def create_guest_booking(request):
    return render(request, '../templates/create_booking.html')

