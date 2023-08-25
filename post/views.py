from django.shortcuts import render
from rest_framework import viewsets
from post.models import Post
from account.models import Univ, User
from post.serializers import PostSerializer, AddPostSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status
from rest_framework.response import Response

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# post 1. 글 작성

@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def add_post(request):
    user = request.user
    univ = user.univ_id
    univ_id = Univ.objects.get(id=univ)

    # 프론트엔드로부터 받는 정보
    content = content

    ballad_tag =  ballad_tag
    dance_tag = dance_tag
    rap_tag =  rap_tag
    RandB_tag =  RandB_tag
    indie_tag =  indie_tag
    rock_tag = rock_tag

    music_name1 = music_name1
    music_url1 = music_url1
    thumnail1 = thumnail1
    music_name2 = music_name2
    music_url2 = music_url2
    thumnail2 = thumnail2
    music_name3 = music_name3
    music_url3 = music_url3
    thumnail3 = thumnail3
    music_name4 = music_name4
    music_url4 = music_url4
    thumnail4 = thumnail4
    music_name5 = music_name5
    music_url5 = music_url5
    thumnail5 = thumnail5
    music_name6 = music_name6
    music_url6 = music_url6
    thumnail6 = thumnail6
    music_name7 = music_name7
    music_url7 = music_url7
    thumnail7 = thumnail7
    music_name8 = music_name8
    music_url8 = music_url8
    thumnail8 = thumnail8
    music_name9 = music_name9
    music_url9 = music_url9
    thumnail9 = thumnail9
    music_name10 = music_name10
    music_url10 = music_url10
    thumnail10 = thumnail10

    post = Post(
    user_id = user,
    univ_id = univ_id,
    content = content,

    ballad_tag =  ballad_tag,
    dance_tag = dance_tag,
    rap_tag =  rap_tag,
    RandB_tag =  RandB_tag,
    indie_tag =  indie_tag,
    rock_tag = rock_tag,
    music_name1 = music_name1,
    music_url1 = music_url1,
    thumnail1 = thumnail1,
    music_name2 = music_name2,
    music_url2 = music_url2,
    thumnail2 = thumnail2,
    music_name3 = music_name3,
    music_url3 = music_url3,
    thumnail3 = thumnail3,
    music_name4 = music_name4,
    music_url4 = music_url4,
    thumnail4 = thumnail4,
    music_name5 = music_name5,
    music_url5 = music_url5,
    thumnail5 = thumnail5,
    music_name6 = music_name6,
    music_url6 = music_url6,
    thumnail6 = thumnail6,
    music_name7 = music_name7,
    music_url7 = music_url7,
    thumnail7 = thumnail7,
    music_name8 = music_name8,
    music_url8 = music_url8,
    thumnail8 = thumnail8,
    music_name9 = music_name9,
    music_url9 = music_url9,
    thumnail9 = thumnail9,
    music_name10 = music_name10,
    music_url10 = music_url10,
    thumnail10 = thumnail10,
    )

    post.save()

    serializer = AddPostSerializer(post)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

# post 2. 글 삭제
@api_view(['DELETE'])
@permission_classes((permissions.IsAuthenticated,))
def delete_post(request):
    user = request.user

    try:
        post_id = request.data.get('post_id')
        post = Post.objects.get(id=post_id, user_id=user)
        post.delete()
        return Response({"information": "delete post"}, status=status.HTTP_204_NO_CONTENT)
    except Post.DoesNotExist:
        return Response({"error": "Post not found"},status=status.HTTP_404_NOT_FOUND)

# post 3. 전체 글 조회



