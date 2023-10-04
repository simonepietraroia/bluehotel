from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home_page, name= 'get_home_page'),
    path('rooms/', views.RoomListView.as_view(), name='room-list'),
    path('booking/create/', views.BookingCreateView.as_view(), name='booking-create'),
    path('booking/<int:pk>/', views.BookingDetailView.as_view(), name='booking-detail'),
]