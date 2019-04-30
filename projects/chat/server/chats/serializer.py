from rest_framework import serializers
from .models import Chat, Message, UserChat


class UserChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChat
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('content', )


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'
