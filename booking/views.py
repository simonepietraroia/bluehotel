from django.shortcuts import render
from .models import GuestBooking
from .forms import GuestBookingForm
from django.views.generic.edit import CreateView

def get_home_page(request):
    return render(request, '../templates/index.html')

class CreateGuestBooking(CreateView):
    model = GuestBooking
    form_class = GuestBookingForm
    template_name = 'create_booking.html'
    