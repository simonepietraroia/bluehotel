from django import forms
from .models import GuestBooking

class GuestBookingForm(forms.ModelForm):
    class Meta:
        model = GuestBooking
        fields = ['user', 'email', 'check_in_date', 'check_out_date', 'num_guests', 'room_type']

