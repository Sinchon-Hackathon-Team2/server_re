from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Follow

from .serializers import FollowCreateSerializer,FollowDestroySerializer


@api_view(['POST'])  
def follow_create_view(request):
    if request.method == 'POST':
        followee_id = request.data.get('followee_id')

        if followee_id is None:
            return Response({"error": "followee_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        follower_id = request.user.id 
        data = {'follower_id': follower_id, 'followee_id': followee_id}
        serializer = FollowCreateSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])  
@permission_classes([IsAuthenticated])  
def follow_delete_view(request):
    follower_id = request.user.id
    followee_id = request.data.get('followee_id')
    data={'follower_id':follower_id,'followee_id':followee_id}
    serializer=FollowDestroySerializer(data=data)
    if serializer.is_valid():
        try:
            follow_instance = Follow.objects.get(follower_id=follower_id, followee_id=followee_id)
        except Follow.DoesNotExist:
            return Response({"error": "Follow instance not found."}, status=status.HTTP_404_NOT_FOUND)
        follow_instance.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

