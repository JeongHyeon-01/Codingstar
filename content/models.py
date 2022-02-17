from django.db import models

# Create your models here.



class Feed(models.Model):
    content       = models.TextField() #글내용
    image         = models.TextField() #피드이미지
    email         = models.EmailField(default='') #글쓴이



class FeedLike(models.Model):
    feed_id = models.IntegerField()
    email = models.CharField(max_length=30, blank=True, null=True)
    is_like = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=['feed_id']),
            models.Index(fields=['email']),
        ]


class Reply(models.Model):
    feed_id = models.IntegerField(default=0)
    # nickname = models.CharField(max_length=30, blank=True, null=True)
    reply_content = models.TextField()
    email = models.EmailField(verbose_name='email', max_length=100, blank=True, null=True)


class Bookmark(models.Model):
    feed_id = models.IntegerField(default=0)
    email = models.EmailField(default='')
    is_marked = models.BooleanField(default=True)