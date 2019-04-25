from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User



def index(request):
    return None


@login_required
@require_http_methods(['POST'])
def toggle_friend(request, user_id):
    me = request.user
    friend = get_object_or_404(User, id=user_id)

    return None