from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, blank=False)
    friendings = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='friendeds', blank=True)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def created_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)

#  https://cjh5414.github.io/django-rest-framework-token-authentication/
#  https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
