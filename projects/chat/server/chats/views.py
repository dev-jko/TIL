from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
import paho.mqtt.publish as publish
from .models import Chat, Message, UserChat
from .serializer import ChatSerializer, MessageSerializer


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
