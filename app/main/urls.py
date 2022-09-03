from django.urls import path, include 
from .views import *

urlpatterns = [
    path('',main,name='main'),
    path('details/post/<int:id>',post_details,name='post_view'),
    path('category/post/<int:id>',get_post_by_category,name='post_category'),
]