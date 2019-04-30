from django.urls import path
from . import views

app_name = 'chats'

urlpatterns = [
    path('', views.create_chat),
    path('<int:chat_id>/', views.chat),

    path('<int:chat_id>/messages/', views.message),
    path('<int:chat_id>/messages/<int:message_id>/', views.delete_message),

    path('<int:chat_id>/users/', views.get_users),
    path('<int:chat_id>/users/<int:user_id>/', views.user),

    path('<int:chat_id>/users/<user_id>/messages/<int:message_id>/', views.update_last_message),

]
