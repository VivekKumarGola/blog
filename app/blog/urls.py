from turtle import update
from django.urls import path
from .views import * 

urlpatterns = [
    path('dashboard/',dashboard,name='dashboard'),
    path('post/',post,name='post'),
    path('add/post/',add_post,name='add_post'),
    path('update/post/<int:id>/',update_post,name='update_post'),
    path('del/post/<int:id>/',del_post,name='del_post'),
]
