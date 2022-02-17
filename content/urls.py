from django.urls import path
from .views import Main, UploadFeed, Profile, CreateReply, LikeFeed, ToggleBookmark

app_name = 'content'
urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('upload', UploadFeed.as_view(), name='upload'),
    path('profile', Profile.as_view(), name='profile'),
    path('replycreate', CreateReply.as_view(), name='reply_create'),
    path('like', LikeFeed.as_view(), name='like'),
    path('bookmark', ToggleBookmark.as_view(), name='bookmark'),
]
