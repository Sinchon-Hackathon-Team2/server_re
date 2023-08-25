from rest_framework import serializers
from .models import Comment

class CommentBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'


class CommentCreateSerializer(CommentBaseSerializer):
    class Meta(CommentBaseSerializer.Meta):
        fields=['post_id','content','nickName']

class CommentDestroySerializer(CommentBaseSerializer):
    class Meta(CommentBaseSerializer.Meta):
        fields=['user_id','post_id','comment_id']