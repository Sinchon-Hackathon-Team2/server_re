from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Comment

from .serializers import CommentCreateSerializer,CommentDestroySerializer


@api_view(['POST'])
def comment_create_view(request):
    if request.method=='POST':
        post_id=request.data.get('post_id')
        content=request.data.get('content')
        nickName=request.data.get('nickName')

        if post_id is None:
            return Response({"error": "post_id is required."}, status=status.HTTP_400_BAD_REQUEST)
        elif content is None:
            return Response({"error": "content is required."}, status=status.HTTP_400_BAD_REQUEST)

        user_id=request.user.id
        data={'user_id':user_id,'post_id':post_id,'content':content,'nickName':nickName}
        serializer=CommentCreateSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return Response({"information":{"add-comment"},"content":}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def comment_delete_view(request):
    user_id=request.user.id
    post_id=request.data.get('post_id')
    comment_id=request.data.get('comment_id')
    data={'user_id':user_id,'post_id':post_id,'comment_id':comment_id}
    serializer=CommentDestroySerializer(data=data)
    if serializer.is_valid():
        try:
            comment_instance=Comment.objects.get(user_id=user_id,post_id=post_id,comment_id=comment_id)
        except Comment.DoesNotExist:
            return Response({"error": "Comment instance not found."},status=status.HTTP_404_NOT_FOUND)
        comment_instance.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)