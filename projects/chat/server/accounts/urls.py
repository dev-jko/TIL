from django.conf.urls import url
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^api-token-auth/', obtain_auth_token),
    path('login/', views.log_in),
    path('friend/<int:user_id>', views.toggle_friend),
    path('signup/', views.signup),
]

# curl -X POST -d "username=mytest1&password=123" http://localhost:8000/accounts/api-token-auth/
# curl -X POST -d "username=admin&password=123" http://localhost:8000/accounts/api-token-auth/