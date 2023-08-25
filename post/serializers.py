from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

# post API serializer
class AddPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'content', 'ballad_tag', 'dance_tag', 'rap_tag', 'RandB_tag', 'indie_tag', 'rock_tag']

class FollowingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'content', 'ballad_tag', 'dance_tag', 'rap_tag', 'RandB_tag', 'indie_tag', 'rock_tag']
