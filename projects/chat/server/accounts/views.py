from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import UserSerializer, RelationshipSerializer
from .models import Relationship, RelationshipType
from chats.models import Chat
from chats.serializer import ChatSerializer


@api_view(['POST'])
def signup(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        user = serialized.save()
        return Response(serialized.data)
    return Response(serialized.errors)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def user_info(request, user_id):
    user = get_object_or_404(get_user_model(), id=user_id)
    if user == request.user:
        serialized = UserSerializer(instance=user)
        return Response(data=serialized.data, status=200)
    return Response(status=400)


def _toggle_relationship(request, user_id, target_user_id, type_name):
    user = get_object_or_404(get_user_model(), id=user_id)
    target = get_object_or_404(get_user_model(), id=target_user_id)
    if user == request.user and user != target:
        relationship_set = Relationship.objects.filter(user=user, target_user=target)
        if request.method == 'POST' and not relationship_set:
            relationship = Relationship()
            relationship.user = user
            relationship.target_user = target
            relationship.relationship_type = RelationshipType.objects.get(type_name=type_name)
            relationship.save()
            serialized = RelationshipSerializer(instance=relationship)
            return Response(data=serialized.data, status=200)
        elif request.method == 'DELETE' and relationship_set:
            relationship_set[0].delete()
            return Response(status=200)
    return Response(status=400)


@api_view(['POST', 'DELETE'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def toggle_friend(request, user_id, friend_id):
    return _toggle_relationship(request, user_id, friend_id, 'friend')


@api_view(['POST', 'DELETE'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def toggle_block(request, user_id, block_id):
    return _toggle_relationship(request, user_id, block_id, 'block')


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def friends(request, user_id):
    user = get_object_or_404(get_user_model(), id=user_id)
    if user == request.user:
        users = []
        for rs in Relationship.objects.filter(user=user,
                                              relationship_type=RelationshipType.objects.get(type_name='friend')):
            users.append(rs.target_user)
        serialized = UserSerializer(instance=users, many=True)
        return Response(data=serialized.data, status=200)
    return Response(status=400)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def blocks(request, user_id):
    user = get_object_or_404(get_user_model(), id=user_id)
    if user == request.user:
        users = []
        for rs in Relationship.objects.filter(user=user,
                                              relationship_type=RelationshipType.objects.get(type_name='block')):
            users.append(rs.target_user)
        serialized = UserSerializer(instance=users, many=True)
        return Response(data=serialized.data, status=200)
    return Response(status=400)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def chat(request, user_id):
    user = get_object_or_404(get_user_model(), id=user_id)
    if user == request.user:
        chats = []
        for rs in user.userchat_set.all():
            chats.append(rs.chat)
        serialized = ChatSerializer(instance=chats, many=True)
        return Response(data=serialized.data, status=200)
    return Response(status=400)
