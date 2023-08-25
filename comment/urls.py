from django.urls import path, include
from . import views

urlpatterns = [
    path('add-comment/',views.comment_create_view, name='comment_create'),
   path('delete-comment/', views.comment_delete_view, name='comment_delete'),
]