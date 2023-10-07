from django.db import models
from django.contrib.auth.models import User

ROOM_CHOICES = ((0,'1 Bed'), (1, '2 Bed'))
class GuestBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    num_guests = models.PositiveIntegerField()
    room_type = models.IntegerField(choices=ROOM_CHOICES)


    def __str__(self):
        return self.user
