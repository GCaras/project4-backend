from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('blogposts/', views.BlogPostList.as_view(), name="blogpost_list"),
    path('blogposts/<int:pk>', views.BlogPostDetail.as_view(), name="blogpost_detail")
]