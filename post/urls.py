# from django.conf import settings
# from django.conf.urls.static import static
from django.contrib import admin
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
    path('following-list/', following_list, name='following-list'),
    path('tag-list/<str:hashtag_name>/', tag_list, name='tag-list'),
    path('my-post/', my_post, name='my-post'),

    path('searchYoutube/', serchMusic, name='search_Youtube'),


]