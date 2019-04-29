from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
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


@api_view(['POST'])
def log_in(request):
    # print(request.POST)
    # print(request.POST.get('username'))
    # print(request.POST.get('password'))
    # user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
    # print('**********************************************************')
    # print('**********************************************************')
    # print('**********************************************************')
    # print('**********************************************************')
    # print('**********************************************************')
    # print(user)
    # print(request.user)
    # token = get_object_or_404(Token, user=request.user)
    # return Response({'token': token}, status=200)
    return None


@api_view(['POST'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def toggle_friend(request, user_id):
    me = request.user
    friend = get_object_or_404(User, id=user_id)

    return None
