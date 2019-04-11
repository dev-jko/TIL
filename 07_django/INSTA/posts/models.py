from django.db import models
import os

ENV = os.environ.get('ENVIRONMENT', 'development')
if ENV == 'development':
    from faker import Faker


class Post(models.Model):
    content = models.CharField(max_length=140)
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    if ENV == 'development':
        @classmethod
        def dummy(cls, n):
            faker = Faker()
            for _ in range(n):
                cls.objects.create(content=faker.text(120))
