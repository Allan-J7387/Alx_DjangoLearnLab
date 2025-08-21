from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()

class UserMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class CommentSerializer(serializers.ModelSerializer):
    author = UserMiniSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']

    def create(self, validated_data):
        # author comes from request.user in the viewset
        return Comment.objects.create(**validated_data)


class PostSerializer(serializers.ModelSerializer):
    author = UserMiniSerializer(read_only=True)
    comments_count = serializers.IntegerField(read_only=True)
    # Optional: include a few latest comments inline
    latest_comments = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = [
            'id', 'author', 'title', 'content',
            'created_at', 'updated_at',
            'comments_count', 'latest_comments'
        ]
        read_only_fields = ['author', 'created_at', 'updated_at', 'comments_count', 'latest_comments']

    def get_latest_comments(self, obj):
        qs = obj.comments.order_by('-created_at')[:3]
        return CommentSerializer(qs, many=True).data

from .models import Post, Comment, Like

class LikeSerializer(serializers.ModelSerializer):
    user = UserMiniSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'post', 'user', 'created_at']
        read_only_fields = ['user', 'created_at']
