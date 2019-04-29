from django.urls import path
from . import views

app_name = 'chats'

urlpatterns = [
    path('', views.create_chat),
    path('<int:chat_id>/', views.chat),

    path('<int:chat_id>/messages/', views.message),

]
