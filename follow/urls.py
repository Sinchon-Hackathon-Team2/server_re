from django.urls import path, include
from . import views

urlpatterns = [
   path('add-followee/',views.follow_create_view, name='follow_create'),
   path('delete-followee/', views.follow_delete_view, name='follow_delete'),
]