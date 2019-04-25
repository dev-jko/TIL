from django.urls import path
from . import views

app_name = 'mton'

urlpatterns = [
    path('', views.index, name='index'),
]