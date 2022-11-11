from django.db import models
from django.conf import settings


class Category(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=221)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/')
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

