from django.shortcuts import render
from .models import Feed, Reply, FeedLike, Bookmark
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
import os
from codingsta.settings import MEDIA_ROOT
from uuid import uuid4
from user.models import User


class Main(APIView):
    def get(self, request):
        email = request.session.get('email', None)
        if email is None:
            return render(request, "user/signin.html")

        user = User.objects.filter(email=email).first()
        if user is None:
            return render(request, "user/signin.html")
        feed_object_feed_list = Feed.objects.all().order_by('-id')
        feed_list = []
        for feed in feed_object_feed_list:
            user = User.objects.filter(email=feed.email).first()
            reply_object_list = Reply.objects.filter(feed_id=feed.id)
            reply_list = []
            for reply in reply_object_list:
                user = User.objects.filter(email=reply.email).first()
                reply_list.append(dict(feed_id=feed.id,
                                       reply_content=reply.reply_content,
                                       nickname=user.nickname))
            like_count = FeedLike.objects.filter(feed_id=feed.id, is_like=True).count()
            is_liked = FeedLike.objects.filter(feed_id=feed.id, email=email, is_like=True).exists()
            is_marked = Bookmark.objects.filter(feed_id=feed.id, email=email, is_marked=True).exists()
            feed_list.append(dict(id=feed.id,
                                  image=feed.image,
                                  content=feed.content,
                                  like_count=like_count,
                                  profile_img=user.profile_img,
                                  nickname=user.nickname,
                                  name=user.name,
                                  reply_list=reply_list,
                                  is_liked=is_liked,
                                  is_marked=is_marked
                                  ))

        return render(request, './content/main.html', context=dict(feed_list=feed_list, user=user))


class UploadFeed(APIView):
    def post(self, request):
        file = request.FILES['file']
        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        content = request.data.get('content')
        image = uuid_name
        email = request.session.get('email', None)

        Feed.objects.create(content=content, image=image, email=email, like_count=0)

        return Response(status=200)


class Profile(APIView):
    def get(self, request):

        email = request.session.get('email', None)

        if email is None:
            return render(request, "user/signin.html")

        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request, "user/signin.html")

        feed_list = Feed.objects.filter(email=email)
        like_list = list(FeedLike.objects.filter(email=email, is_like=True).values_list('feed_id', flat=True))
        like_feed_list = Feed.objects.filter(id__in=like_list)
        bookmark_list = list(Bookmark.objects.filter(email=email, is_marked=True).values_list('feed_id', flat=True))
        bookmark_feed_list = Bookmark.objects.filter(id__in=bookmark_list)
        return render(request, './mypage/index.html', context=dict(feed_list=feed_list, like_feed_list=like_feed_list,
                                                                   bookmark_feed_list=bookmark_feed_list, user=user))


class UploadReply(APIView):
    def post(self, request):
        feed_id = request.session.get('feed_id', None)
        reply_content = request.session.get('reply_content', None)
        email = request.session.get('email', None)

        Reply.objects.create(feed_id=feed_id, reply_content=reply_content, email=email)
        return Response(status=200)


class CreateReply(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id')
        user_id = request.data.get('user_id')
        reply_content = request.data.get('reply_content')
        email = request.data.get('email')
        Reply.objects.create(feed_id=feed_id,
                             user_id=user_id,
                             reply_content=reply_content,
                             email=email
                             )

        return Response(status=200, data=dict(message='댓글 작성 완료.'))


class LikeFeed(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id')
        email = request.data.get('email')
        favorite_text = request.data.get('favorite_text', 'True')

        if favorite_text == "favorite_border":
            is_like = True
        else:
            is_like = False

        email = request.session.get('email', None)

        like = FeedLike.objects.filter(feed_id=feed_id, email=email).first()

        if like:
            like.is_like = is_like
            like.save()
        else:
            FeedLike.objects.create(feed_id=feed_id, is_like=is_like, email=email)

        return Response(status=200)


class ToggleBookmark(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id')
        bookmark_text = request.data.get('bookmark_text', 'True')
        email = request.session.get('email', None)
        if bookmark_text == "bookmark_border":
            is_marked = True
        else:
            is_marked = False

        bookmark = Bookmark.objects.filter(feed_id=feed_id, email=email).first()

        if bookmark:
            bookmark.is_marked = is_marked
            bookmark.save()
        else:
            Bookmark.objects.create(feed_id=feed_id, is_marked=is_marked, email=email)

        return Response(status=200)
