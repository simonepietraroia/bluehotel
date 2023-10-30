from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from .models import GuestBooking
from .forms import GuestBookingForm
from .views import GuestBookingListView, GuestBookingCreateView, GuestBookingUpdateView, GuestBookingDeleteView

class GuestBookingViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.guest_booking = GuestBooking.objects.create(
            user=self.user,
            guest_name='John',
            email='john@gmail.com.com',
            check_in_date='2023-01-01',
            check_out_date='2023-01-05',
            num_guests=2,
            room_type=0  
        )

    def test_home_page_view(self):
        request = self.factory.get(reverse('home'))
        response = get_home_page(request)
        self.assertEqual(response.status_code, 200)

    def test_guest_booking_list_view(self):
        request = self.factory.get(reverse('booking_list'))
        request.user = self.user
        response = GuestBookingListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn('bookings', response.context)

    def test_guest_booking_create_view(self):
        request = self.factory.get(reverse('create_booking'))
        request.user = self.user
        response = GuestBookingCreateView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_guest_booking_update_view(self):
        request = self.factory.get(reverse('update_booking', args=[self.guest_booking.pk]))
        response = GuestBookingUpdateView.as_view()(request, pk=self.guest_booking.pk)
        self.assertEqual(response.status_code, 200)

    def test_guest_booking_delete_view(self):
        request = self.factory.get(reverse('delete_booking', args=[self.guest_booking.pk]))
        response = GuestBookingDeleteView.as_view()(request, pk=self.guest_booking.pk)
        self.assertEqual(response.status_code, 200)

    def test_guest_booking_form_valid_submission(self):
        request = self.factory.post(reverse('create_booking'), {
            'guest_name': 'john',
            'email': 'john@gmail.com',
            'check_in_date': '2023-01-01',
            'check_out_date': '2023-01-05',
            'num_guests': 3,
            'room_type': 1  
        })
        request.user = self.user
        response = GuestBookingCreateView.as_view()(request)
        self.assertEqual(response.status_code, 302)  
