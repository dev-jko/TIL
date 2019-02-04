from django.urls import path
from . import views

app_name = 'workshop19'

urlpatterns = [
    path('', views.index, name='student_index'),
    path('<int:id>/', views.detail, name='student_detail'),
    path('new/', views.new, name='student_new'),
    path('update/', views.update, name='student_update'),
    path('delete/', views.delete, name='student_delete'),
]
