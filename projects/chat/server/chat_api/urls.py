from django.urls import path
from . import views

app_name = 'chat_api'

urlpatterns = [
    path('<int:chat_room_id>/message/', views.message, name='send_message'),
]
