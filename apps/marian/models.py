

from django.db import models
from django.utils import timezone

from apps.accounts.models import Account
from config import settings


class Service(models.Model):
    place = models.CharField(max_length=211)
    title = models.CharField(max_length=211)
    image = models.ImageField(upload_to='service/')
    content = models.TextField()

    def __str__(self):
        return self.title


class Room(models.Model):
    DAY = (
        (0, 'day'),
        (1, 'night')
    )
    title = models.CharField(max_length=211, null=True)
    image = models.ImageField(upload_to='rooms/')
    day = models.IntegerField(choices=DAY, default=0)
    price = models.IntegerField()

    def __str__(self):
        return self.title


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    package = models.ForeignKey(Room, on_delete=models.CASCADE)
    email = models.EmailField()
    show=models.BooleanField(default=True)
    phone = models.CharField(max_length=255)
    s_d = models.DateField(null=True)
    e_d = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username