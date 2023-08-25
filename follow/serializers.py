from rest_framework import serializers
from .models import Follow

class FollowBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Follow
        fields='__all__'


class FollowCreateSerializer(FollowBaseSerializer):
    class Meta(FollowBaseSerializer.Meta):
        fields=['followee_id']

class FollowDestroySerializer(FollowBaseSerializer):
    class Meta(FollowBaseSerializer.Meta):
        fields=['follower_id','followee_id']