from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.conf import settings


class Chat(TimeStampedModel):
    pass


class Message(TimeStampedModel):
    content = models.CharField(max_length=500)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class UserChat(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    last_message = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True)
