from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import GuestBooking

class GuestBookingForm(forms.ModelForm):
    class Meta:
        model = GuestBooking
        fields = ['name', 'email', 'check_in_date', 'check_out_date', 'num_guests', 'room_type']

    def __init__(self, *args, **kwargs):
        super(GuestBookingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'email',
            'check_in_date',
            'check_out_date',
            'num_guests',
            'room_type',
            Submit('submit', 'Create Booking')
        )
