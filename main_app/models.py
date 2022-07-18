from django.db import models
from django.urls import reverse

RATINGS = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
)
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

class Comment(models.Model):
    rating = models.IntegerField(
        choices=RATINGS,
        default=RATINGS[0][0])
    comment = models.TextField(max_length=1000)

    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"Rating: {self.get_rating_display()} Comment: {self.comment}"