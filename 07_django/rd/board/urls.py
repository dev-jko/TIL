from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.board_list, name='board_list'),
    path('detail/<int:id>/', views.board_detail, name='board_detail'),
    path('delete/<int:id>/', views.board_delete, name='board_delete'),
]
