from django import forms
from .models import GuestBooking

class GuestBookingForm(forms.ModelForm):
    class Meta:
        model = GuestBooking
        fields = ['user', 'email', 'check_in_date', 'check_out_date', 'num_guests', 'room_type']

    def clean(self):
        cleaned_data = super().clean()
        check_in_date = cleaned_data.get('check_in_date')
        check_out_date = cleaned_data.get('check_out_date')

        if check_in_date and check_out_date and check_in_date >= check_out_date:
            self.add_error('check_in_date', 'Check-in date must be before check-out date')
