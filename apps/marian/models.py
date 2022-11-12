from django.db import models


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
    title = models.CharField(max_length=211)
    image = models.ImageField(upload_to='rooms/')
    day = models.IntegerField(choices=DAY, default=0)
    price = models.IntegerField()

    def __str__(self):
        return self.title