from django.contrib.auth.forms import UserCreationForm
from .models import User


class CustomUserCreationsForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username', )
