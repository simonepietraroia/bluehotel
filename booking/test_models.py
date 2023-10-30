from django.test import TestCase
from django.contrib.auth.models import User
from your_app.models import GuestBooking, ROOM_CHOICES

class GuestBookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_create_guest_booking(self):
        guest_booking = GuestBooking.objects.create(
            user=self.user,
            guest_name='John',
            email='john@gmail.com',
            check_in_date='2023-01-01',
            check_out_date='2023-01-05',
            num_guests=2,
            room_type=0  
        )

        self.assertEqual(guest_booking.guest_name, 'John')
        self.assertEqual(guest_booking.email, 'john@gmail.com')
        self.assertEqual(guest_booking.check_in_date, '2023-01-01')
        self.assertEqual(guest_booking.check_out_date, '2023-01-05')
        self.assertEqual(guest_booking.num_guests, 2)
        self.assertEqual(guest_booking.room_type, 0)

    def test_model_str_method(self):
        guest_booking = GuestBooking.objects.create(
            user=self.user,
            guest_name='John',
            email='john@gmail.com',
            check_in_date='2023-01-01',
            check_out_date='2023-01-05',
            num_guests=2,
            room_type=1  
        )

        self.assertEqual(str(guest_booking), 'John')

    def test_model_choices(self):
        self.assertEqual(ROOM_CHOICES[0], (0, '1 Bed'))
        self.assertEqual(ROOM_CHOICES[1], (1, '2 Bed'))
