from django.conf.urls import url
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup),
    url(r'^api-token-auth/', obtain_auth_token),

    path('<int:user_id>/', views.user_info),
    path('<int:user_id>/friends/', views.friends),
    path('<int:user_id>/friends/<int:friend_id>/', views.toggle_friend),
    path('<int:user_id>/blocks/', views.blocks),
    path('<int:user_id>/blocks/<int:block_id>/', views.toggle_block),

    path('<int:user_id>/chats/', views.chat),
]

