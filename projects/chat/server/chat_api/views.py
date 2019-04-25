from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
import paho.mqtt.publish as publish



@api_view(['GET', 'POST'])
def message(request, chat_room_id):
    # chat_room = get_object_or_404(, id=chat_room_id)
    return None
