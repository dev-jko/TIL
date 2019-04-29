from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver


class RelationshipType(models.Model):
    type_name = models.CharField(max_length=50, unique=True)


class Relationship(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    target_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='targeted')
    relationship_type = models.ForeignKey(RelationshipType, on_delete=models.SET_DEFAULT, default=0)


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, blank=False)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def created_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.get_or_create(user=instance)
