from django.urls import path, include
from rest_framework.routers import DefaultRouter
from post.views import *

router = DefaultRouter()
router.register('post', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('add-post/', add_post, name='add-post'),
    path('delete-post/', delete_post, name='delete-post'),
    path('post-list/', post_list, name='post-list'),
    path('following-list', following_list, name='following-list'),

]