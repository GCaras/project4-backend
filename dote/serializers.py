from rest_framework import serializers

from .models import User, BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('title', 'body', 'user', 'id')

class UserSerializer(serializers.ModelSerializer):

    # blogposts = BlogPostSerializer(many=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'id')