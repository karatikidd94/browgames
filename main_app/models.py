from django.db import models
from django.urls import reverse

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    link = models.CharField(max_length=1000)
    creator = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})
