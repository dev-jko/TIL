from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
import paho.mqtt.publish as publish
from .models import Chat, Message, UserChat
from .serializer import ChatSerializer, MessageSerializer
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


# TODO 테스트 해보기
@api_view(['PATCH'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def delete_message(request, chat_id, message_id):
    get_object_or_404(Chat, id=chat_id)
    message = get_object_or_404(Message, id=message_id)
    if request.user == message.user:
        message.content = '삭제된 메세지 입니다.'
        message.save()
        return Response(status=200)
    return Response(status=400)


# TODO 테스트 해보기
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def user(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    users = chat.userchat_set.filter(chat=chat)
    serialized = UserSerializer(users, many=True)
    return Response(data=serialized.data)
