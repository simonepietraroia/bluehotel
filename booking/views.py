from django.shortcuts import render, redirect
from .models import GuestBooking
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import GuestBookingForm
from django.urls import reverse, reverse_lazy

def get_home_page(request):
    return render(request, '../templates/index.html')
   
class GuestBookingListView(ListView):
    model = GuestBooking
    template_name = 'guestbooking_list.html'
    context_object_name = 'bookings'

class GuestBookingCreateView(CreateView):
    model = GuestBooking
    template_name = 'create_booking.html'
    form_class = GuestBookingForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('get_home_page')
            
class GuestBookingUpdateView(UpdateView):
    model = GuestBooking
    template_name = 'guestbooking/guestbooking_form.html'
    form_class = GuestBookingForm
    success_url = '/guestbookings/'

class GuestBookingDeleteView(DeleteView):
    model = GuestBooking
    template_name = 'guestbooking/booking_confirm_delete.html'
    success_url = reverse_lazy('booking_list')