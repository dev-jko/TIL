from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.id} {self.title}'
