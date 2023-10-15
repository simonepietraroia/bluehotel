from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import GuestBooking
from .forms import GuestBookingForm

def get_home_page(request):
    return render(request, '../templates/index.html')

class GuestBookingView(View):
    template_name = 'create_booking.html'

    def get(self, request, booking_id=None):
        if booking_id:
            booking = get_object_or_404(GuestBooking, pk=booking_id)
            form = GuestBookingForm(instance=booking)
        else:
            form = GuestBookingForm()

        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, booking_id=None):
        if booking_id:
            booking = get_object_or_404(GuestBooking, pk=booking_id)
            form = GuestBookingForm(request.POST, instance=booking)
        else:
            form = GuestBookingForm(request.POST)

        if form.is_valid():
            booking = form.save()
            return redirect('booking_confirmation')
        else:
            context = {
                'form': form,
            }
            return render(request, self.template_name, context)

