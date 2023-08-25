from django.urls import path, include
from . import views

urlpatterns = [
    path('request/', views.requestCode, name='RequestCode'),
    path('check/', views.checkCode, name='CheckCode'),
    path('make/', views.makeUniv, name='MakeUniv'),
]