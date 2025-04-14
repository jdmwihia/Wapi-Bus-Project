from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Seat(models.Model):
    number = models.IntegerField(unique=True)
    is_booked = models.BooleanField(default=False)
    booked_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
     return f"Seat {self.number}"