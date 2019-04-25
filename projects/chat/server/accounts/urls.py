from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('friend/<int:user_id>', views.toggle_friend, name='toggle_friend'),


]
