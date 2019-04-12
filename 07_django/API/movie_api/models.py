from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)

    @classmethod
    def dummy(cls, n):
        from faker import Faker
        f = Faker()
        for _ in range(n):
            cls.objects.create(title=f.catch_phrase())
