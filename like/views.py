from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Like

from .serializers import LikeBaseSerializer


@api_view(['POST'])
def like_create_delete_view(request):
    if request.method=='POST':
        user_id=request.user.id
        post_id=request.data.get('post_id')
        data={'user_id':user_id,'post_id':post_id}
        serializer=LikeBaseSerializer(data=data)
        if serializer.is_valid():
            try:
                like_instance=Like.objects.get(user_id=user_id,post_id=post_id)
                like_instance.delete()
            except Like.DoesNotExist:
                serializer.save()
                return Response({"information":"add-like"})
            return Response({"information":"delete-like"})
        return Response(serializer.errors,status=400)
            






