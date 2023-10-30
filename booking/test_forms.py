from django.test import TestCase
from .forms import GuestBookingForm

class GuestBookingFormTest(TestCase):
    def test_form_fields(self):
        form = GuestBookingForm()
        self.assertTrue('guest_name' in form.fields)
        self.assertTrue('email' in form.fields)
        self.assertTrue('check_in_date' in form.fields)
        self.assertTrue('check_out_date' in form.fields)
        self.assertTrue('num_guests' in form.fields)
        self.assertTrue('room_type' in form.fields)

    def test_form_validation(self):
        data = {
            'guest_name': 'john',
            'email': 'john@gmail.com',
            'check_in_date': '2023-01-01',
            'check_out_date': '2023-01-05',
            'num_guests': 2,
            'room_type': '1 Bed'
        }
        form = GuestBookingForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        data = {
            'guest_name': '',
            'email': 'notemail',
            'check_in_date': '2023-01-01',
            'check_out_date': '2023-01-05',
            'num_guests': -1,
            'room_type': 'Invalid'
        }
        form = GuestBookingForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_submission(self):
        data = {
            'guest_name': 'John',
            'email': 'john@gmail.com',
            'check_in_date': '2023-01-01',
            'check_out_date': '2023-01-05',
            'num_guests': 2,
            'room_type': '1 Bed'
        }
        form = GuestBookingForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_submission_without_data(self):
        form = GuestBookingForm()
        self.assertFalse(form.is_valid())
