from django.db import models

from config import settings


class Wallet(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.author.username
