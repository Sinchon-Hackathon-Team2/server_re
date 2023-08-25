from django.shortcuts import render
from rest_framework import viewsets
from post.models import Post
from account.models import Univ, User
from follow.models import Follow
from post.serializers import PostSerializer, AddPostSerializer, PostListSerializer, FollowingListSerializer, TagListSerializer, MyPostSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status
from rest_framework.response import Response
import requests
import json

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# post 1. 글 작성 (로그인)

@api_view(['POST'])
# @permission_classes((permissions.IsAuthenticated,))
def add_post(request):
    user_id = request.data.get('user_id')
    univ_id = request.data.get('univ_id')
    user_id = User.objects.get(id=user_id)
    univ_id = Univ.objects.get(univ_id=univ_id)
    # user = request.user
    # univ = user.univ_id
    # univ_id = Univ.objects.get(id=univ)

    # 프론트엔드로부터 받는 정보
    content = request.data.get('content')

    ballad_tag =  request.data.get('ballad_tag')
    dance_tag = request.data.get('dance_tag')
    rap_tag =  request.data.get('rap_tag')
    RandB_tag =  request.data.get('RandB_tag')
    indie_tag =  request.data.get('indie_tag')
    rock_tag = request.data.get('rock_tag')

    music_name1 = request.data.get('music_name1')
    music_url1 = request.data.get('music_url1')
    thumnail1 = request.data.get('thumnail1')
    music_name2 = request.data.get('music_name2')
    music_url2 = request.data.get('music_url2')
    thumnail2 = request.data.get('thumnail2')
    music_name3 = request.data.get('music_name3')
    music_url3 = request.data.get('music_url3')
    thumnail3 = request.data.get('thumnail3')
    music_name4 = request.data.get('music_name4')
    music_url4 = request.data.get('music_url4')
    thumnail4 = request.data.get('thumnail4')
    music_name5 = request.data.get('music_name5')
    music_url5 = request.data.get('music_url5')
    thumnail5 = request.data.get('thumnail5')
    music_name6 = request.data.get('music_name6')
    music_url6 = request.data.get('music_url6')
    thumnail6 = request.data.get('thumnail6')
    music_name7 = request.data.get('music_name7')
    music_url7 = request.data.get('music_url7')
    thumnail7 = request.data.get('thumnail7')
    music_name8 = request.data.get('music_name8')
    music_url8 = request.data.get('music_url8')
    thumnail8 = request.data.get('thumnail8')
    music_name9 = request.data.get('music_name9')
    music_url9 = request.data.get('music_url9')
    thumnail9 = request.data.get('thumnail9')
    music_name10 = request.data.get('music_name10')
    music_url10 = request.data.get('music_url10')
    thumnail10 = request.data.get('thumnail10')

    post = Post(
    user_id = user_id,
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

    # post.save()

    serializer = AddPostSerializer(post)
    
    return Response(serializer.data, status=status.HTTP_201_CREATED)

# post 2. 글 삭제 (로그인)
@api_view(['DELETE'])
# @permission_classes((permissions.IsAuthenticated,))
def delete_post(request):
    user = request.user
    user_id = request.data.get('user_id')
    univ_id = request.data.get('univ_id')

    try:
        post_id = request.data.get('post_id')
        post = Post.objects.get(id=post_id, user_id=user)
        post.delete()
        return Response({"information": "delete post"}, status=status.HTTP_204_NO_CONTENT)
    except Post.DoesNotExist:
        return Response({"error": "Post not found"},status=status.HTTP_404_NOT_FOUND)

# post 3. 전체 글 조회
@api_view(['GET'])
# @permission_classes((permissions.IsAuthenticated,))
def post_list(request):
    user = request.user
    user_id = request.data.get('user_id')
    univ_id = request.data.get('univ_id')

    # response: post_id, content, tag

    all_post = Post.objects.all()
    serializer = PostListSerializer(all_post, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

# post 4. 팔로우한 사람의 글만 조회
@api_view(['GET'])
# @permission_classes((permissions.IsAuthenticated,))
def following_list(request):
    user = request.user
    user_id = request.data.get('user_id')
    univ_id = request.data.get('univ_id')

    followers = Follow.objects.filter(follower_id = user).values_list('followee_id', flat=True)
    following_posts = Post.objects.filter(user_id__in = followers)

    serializer = FollowingListSerializer(following_posts, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

# post 5. 태그별 조회
@api_view(['GET'])
# @permission_classes((permissions.AllowAny,))
def tag_list(request, tag_name):
    user_id = request.data.get('user_id')
    univ_id = request.data.get('univ_id')
    if tag_name == 'ballad_tag':
        tag_posts = Post.objects.filter(ballad_tag = True)
    elif tag_name == 'dance_tag':
        tag_posts = Post.objects.filter(dance_tag = True)
    elif tag_name == 'rap_tag':
        tag_posts = Post.objects.filter(rap_tag = True)
    elif tag_name == 'RandB_tag':
        tag_posts = Post.objects.filter(RandB_tag = True)
    elif tag_name == 'indie_tag':
        tag_posts = Post.objects.filter(indie_tag = True)
    elif tag_name == 'rock_tag':
        tag_posts = Post.objects.filter(rock_tag = True)
    
    serializer = TagListSerializer(tag_posts, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

# post 6. 내 포스트 조회
@api_view(['GET'])
# @permission_classes((permissions.IsAuthenticated,))
def my_post(request):
    user = request.user
    user_id = request.data.get('user_id')
    univ_id = request.data.get('univ_id')
    my_posts = Post.objects.filter(user_id = user)

    serializer = MyPostSerializer(my_posts, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

# # post 7. 포스트 상세 조회
# @api_view(['GET'])
# @permission_classes((permissions.IsAuthenticated,))
# def postDetail(request):
#     user_id = request.data.get('user_id')
#     post_id = request.data.get('post_id')
#     post = Post.objects.get(post_id=post_id)
#     postData = post.data

#     like= Post.objects.filter(post_id=post_id).values()

#     likeData = list(like)

#     if len(likeData) != 0:
#         postData["isLike"]

#     return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def serchMusic(request):
    word = request.data.get('word')
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "maxResults": 10,
        "q": word,
        "type": "video",
        "key": "AIzaSyAF4CjHKCqwmsV74shNZ2yLWav9bfAJ9p4"
    }

    response = requests.get(url, params=params)

    data = json.loads(response.content)
    videoList = data["items"]

    results = []

    for video in videoList:
        dict = {}
        id = video["id"]["videoId"]

        snippet = video["snippet"]
        title = snippet["title"]
        print(title)
        thumbnail = snippet["thumbnails"]["default"]["url"]
        print(thumbnail)
        channel = snippet["channelTitle"]

        dict = {"title":title, "thumbnail":thumbnail, "channelTitle":channel, "url":f"https://www.youtube.com/watch?v={id}"}

        results.append(dict)


    return Response(results, status=status.HTTP_200_OK)
    # print(data)

