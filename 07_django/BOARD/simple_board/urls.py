from django.urls import path
from . import views

app_name = 'simple_board'

urlpatterns = [
    # url about article
    path('', views.article_list, name='article_list'),
    path('create/', views.article_create, name='article_create'),
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('<int:article_id>/update/', views.article_update, name='article_update'),
    path('<int:article_id>/delete/', views.article_delete, name='article_delete'),

    # url about comment
    path('<int:article_id>/comments/create/', views.comment_create, name='comment_create'),
    path('<int:article_id>/comments/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),

]
