from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
import paho.mqtt.publish as publish
from .models import Chat, Message, UserChat
from .serializer import ChatSerializer, MessageSerializer, UserChatSerializer
from accounts.serializer import UserSerializer


# TODO 채팅방 추가하기
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def create_chat(request):
    chat = Chat()
    chat.save()
    uc = UserChat()
    uc.chat = chat
    uc.user = request.user
    uc.save()
    return Response(data={'test': '성공'})


# TODO 채팅방 삭제하기
@api_view(['DELETE'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def chat(request, chat_id):
    get_object_or_404(Chat, id=chat_id)
    return None


@api_view(['GET', 'POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def message(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    if request.method == 'GET':
        messages = chat.message_set.all()
        print(messages)
        serialized = MessageSerializer(instance=messages, many=True)
        return Response(data=serialized.data)
    else:
        serializer = MessageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user, chat=chat)
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['PATCH'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def delete_message(request, chat_id, message_id):
    get_object_or_404(Chat, id=chat_id)
    message = get_object_or_404(Message, id=message_id)
    if request.user == message.user:
        message.content = '삭제된 메세지 입니다.'
        message.save()
        return Response(MessageSerializer(instance=message).data, status=200)
    return Response(status=400)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def get_users(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    users = chat.userchat_set.filter(chat=chat)
    serialized = UserChatSerializer(users, many=True)
    return Response(data=serialized.data)


@api_view(['POST', 'DELETE'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def user(request, chat_id, user_id):
    chat = get_object_or_404(Chat, id=chat_id)
    user = get_object_or_404(get_user_model(), id=user_id)
    if user == request.user:
        user_chat_set = UserChat.objects.filter(user=user, chat=chat)
        if request.method == 'POST' and not user_chat_set:
            user_chat = UserChat.objects.create(user=user, chat=chat)
            serialized = UserChatSerializer(instance=user_chat)
            return Response(data=serialized.data)
        elif request.method == 'DELETE' and user_chat_set:
            user_chat_set[0].delete()
            return Response(status=200)
    return Response(status=400)


@api_view(['PATCH'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def update_last_message(request, chat_id, user_id, message_id):
    chat = get_object_or_404(Chat, id=chat_id)
    user = get_object_or_404(get_user_model(), id=user_id)
    message = get_object_or_404(Message, id=message_id)
    if user == request.user:
        user_chat = get_object_or_404(UserChat, chat=chat, user=user)
        user_chat.last_message = message
        user_chat.save()
        serialized = UserChatSerializer(instance=user_chat)
        return Response(data=serialized.data, status=200)
    return Response(status=400)
