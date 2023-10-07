from django.shortcuts import render, get_object_or_404, redirect
from .models import GuestBooking
from .forms import GuestBookingForm 

def get_home_page(request):
    return render(request, '../templates/base.html')

def create_guest_booking(request):
    if request.method == 'POST':
        form = GuestBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = GuestBookingForm()
    
    return render(request, 'booking/create_booking.html', {'form': form})

