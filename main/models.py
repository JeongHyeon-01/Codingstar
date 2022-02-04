from django.db import models  # django에서 제공하는 라이브러리
from login import models as user_model # login의 모델에서 작성했던 users 모델을 사용할 겁니다.

class TimeStamedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

# Post 라는 객체는 django의 기본 데이터베이스 모델 기능을 수행할 수 있습니다.
# author는 작성자를 의미합니다. login의 users 모델을 참조합니다.
# image는 사진을 의미합니다. 사진이 저장될 수 있도록 ImageField를 사용합니다.
# caption은 사진에 대한 간략한 설명을 의미합니다.
# image_likes는 post에서 좋아요를 받는 것을 의미하는데, 일단 만들어만 둡니다. 삭제할 수 있음.
# post 객체를 조회할때, 작성자(author)와 간략설명(caption)이 찍히게 합니다.
class Post(TimeStamedModel):
    objects = None
    author = models.ForeignKey(user_model.users, null=True, on_delete=models.CASCADE, related_name='post_author')
    image = models.ImageField(blank=False)
    caption = models.TextField(blank=False)
    image_likes = models.ManyToManyField(user_model.users, blank=True, related_name='post_image_likes')

    def __str__(self):
        return f"{self.author}:{self.caption}"

# comment 라는 객체는 django의 기본 데이터베이스 모델 기능을 수행할 수 있습니다.
# author는 작성자를 의미합니다. login의 users 모델을 참조합니다.
# 여러개의 포스트(posts)는 여러개의 댓글이 달릴 수 있습니다. Post 모델을 참조합니다.
# content는 내용을 의미합니다.
# comment을 조회할 때, 작성자(author)와 내용(content)이 찍히게 합니다.
class Comment(TimeStamedModel):
    author = models.ForeignKey(user_model.users, null=True, on_delete=models.CASCADE, related_name='comment_author')
    posts = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, related_name='comment_post')
    contents = models.TextField(blank=True)

    def __str__(self):
        return f"{self.author}:{self.contents}"