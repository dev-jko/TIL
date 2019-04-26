from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializer import UserSerializer
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def signup(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        user = serialized.save()
        return Response(serialized.data)
    return Response(serialized.errors)


# @api_view(['POST'])
# def log_in(request):
#     login(request)
#     if
#         token = get_object_or_404(Token, user=user)
#         return Response(token)
#     print('로그인 실패')
#     print('로그인 실패')
#     print('로그인 실패')
#     print('로그인 실패')
#     return Response(status=401)


@login_required
@require_http_methods(['POST'])
def toggle_friend(request, user_id):
    me = request.user
    friend = get_object_or_404(User, id=user_id)

    return None


