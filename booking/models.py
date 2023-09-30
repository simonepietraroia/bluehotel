from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User 

class Room(models.Model):
    ROOM_CHOICES = [
        ('type1', 'Type 1'),
        ('type2', 'Type 2'),
    ]

    room_type = models.CharField(
        max_length=10,
        choices=ROOM_CHOICES,
        unique=True,
    )

    def __str__(self):
        return self.get_room_type_display()

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def clean(self):
        conflicting_bookings = Booking.objects.filter(
            room=self.room,
            check_in_date__lte=self.check_out_date,
            check_out_date__gte=self.check_in_date,
        ).exclude(pk=self.pk)

        if conflicting_bookings.exists():
            conflicting_rooms = ', '.join([str(booking.room) for booking in conflicting_bookings])
            raise ValidationError(
                _('This room type is fully booked for the dates you provided. Please select other dates. Conflicting rooms: %s') % conflicting_rooms
            )

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Booking for {self.room} by {self.user} from {self.check_in_date} to {self.check_out_date}'
