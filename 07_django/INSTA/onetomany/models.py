from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel


class MagazineArticle(TimeStampedModel, TitleDescriptionModel):
    content = models.TextField()


class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Writer(TimeStamp):
    name = models.CharField(max_length=150, default='')


class Book(TimeStamp):
    author = models.ForeignKey(Writer, on_delete=models.PROTECT)
    title = models.CharField(max_length=150, default='', unique=True)
    description = models.TextField(default='')


class Comment(TimeStamp):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)


class Chapter(TitleDescriptionModel, TimeStampedModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
