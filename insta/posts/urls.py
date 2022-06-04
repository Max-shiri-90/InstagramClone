from django.urls import path

from .views import PostModelListView, PostModelDetailView


urlpatterns = [
    path('posts-list/', PostModelListView.as_view(), name="posts-list"),
    path('posts-detail/<int:pk>', PostModelDetailView.as_view(), name="posts-detail"),
]
