from django.urls import path, include 
from .views import *

urlpatterns = [
    path('',main,name='main'),
    path('details/post/<int:id>',post_details,name='post_view'),
]