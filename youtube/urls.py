from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('video/', views.video, name='video_detail'),
]
