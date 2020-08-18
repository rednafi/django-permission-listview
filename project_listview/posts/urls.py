# posts/urls.py
from django.urls import path
from .views import PostListByGroup
from rest_framework import request
urlpatterns = [
    path('', PostListByGroup.as_view())
    # path("group_1/view", PostListGroup1.as_view()),
    # path("group_2/view", PostListGroup2.as_view()),

]
