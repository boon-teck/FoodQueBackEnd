from django.urls import path
from accounts.views import *

urlpatterns = [
    path('api/login/', login_user_api, name='login_api_page'),
    path('api/register/', register_user_api, name='register_api_page'),
]