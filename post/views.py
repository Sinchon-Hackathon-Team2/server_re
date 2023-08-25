from django.shortcuts import render
from rest_framework import viewsets
from post.models import Post
from account.models import Univ, User
from post.serializers import PostSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status
from rest_framework.response import Response

class BoardPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer