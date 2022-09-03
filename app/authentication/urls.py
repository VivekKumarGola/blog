from django.urls import path
from .views import *

urlpatterns = [
    path('login/',user_login,name="user_login"),
    path('logout/',logout_user,name="logout_user"),
    path('signup/',register,name="register"),
]
