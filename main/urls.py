from django.urls import path
from . import views

# codingstar/urls.py에는 path('main/', include('main.urls')),
# main/ 요청이 들어오면 Main_feed
# main/create/ 요청이 들어오면 post_create
# main/1/update/ 요청이 들어오면 post_update
# main/1/comment_create/ 요청이 들어오면 comment_create
# main/1/comment_delete/ 요청이 들어오면 comment_delete

urlpatterns = [
    path('main/', views.Main_feed, name='Main_feed'),
    #path('create/', views.post_create, name='post_create'),
    #path('<int:post_id>/update/', views.post_update, name='post_update'),
    #path('<int:post_id>/comment_create/', views.comment_create, name='comment_create'),
    #path('<int:comment_id>/comment_delete/', views.comment_delete, name='comment_delete'),
]