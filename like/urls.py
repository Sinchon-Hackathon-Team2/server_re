from django.urls import path, include
from .  import views

urlpatterns = [
    path('add-delete-like/',views.like_create_delete_view,name="like_create_delete")
]