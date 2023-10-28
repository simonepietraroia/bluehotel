from django.shortcuts import render, redirect
from .models import GuestBooking
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import GuestBookingForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def get_home_page(request):
    return render(request, '../templates/index.html')
   
class GuestBookingListView(LoginRequiredMixin, ListView):
    model = GuestBooking
    template_name = 'guestbooking_list.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return GuestBooking.objects.filter(user=self.request.user)

class GuestBookingCreateView(LoginRequiredMixin, CreateView):
    model = GuestBooking
    template_name = 'create_booking.html'
    form_class = GuestBookingForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('booking_list')
            
class GuestBookingUpdateView(UpdateView):
    model = GuestBooking
    template_name = 'guestbooking_update.html'
    form_class = GuestBookingForm
    
    def get_success_url(self):
        return reverse('booking_list')

class GuestBookingDeleteView(DeleteView):
    model = GuestBooking
    template_name = 'booking_confirm_delete.html'
    success_url = reverse_lazy('booking_list')

    
    def confirm_delete(self):
        return reverse('/booking_list/')