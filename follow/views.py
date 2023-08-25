from django.shortcuts import render
from rest_framework.decorators import api_view, action
from rest_framework import generics, status

from .models import Follow
from .serializers import FollowCreateSerializer,FollowDestroySerializer

class FollowCreateView(generics.CreateAPIView):
    queryset=Follow.objects.all()
    serializer_class=FollowCreateSerializer

class FollowDestroyView(generics.DestroyAPIView):
    queryset=Follow.objects.all()
    serializer_class=FollowDestroySerializer



