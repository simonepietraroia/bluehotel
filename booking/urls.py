from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home_page, name= 'get_home_page'),
    path('guestbookings/', views.GuestBookingListView.as_view(), name='booking-list'),
    path('guestbookings/create/', views.GuestBookingCreateView.as_view(), name='create_booking'),
    path('guestbookings/update/<int:pk>/', views.GuestBookingUpdateView.as_view(), name='update_booking'),
    path('guestbookings/delete/<int:pk>/', views.GuestBookingDeleteView.as_view(), name='delete_booking'),
]