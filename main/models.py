from django.db import models  # django에서 제공하는 라이브러리
from login import models as user_model # login의 모델에서 작성했던 users 모델을 사용할 겁니다.

# Post 라는 객체는 django의 기본 데이터베이스 모델 기능을 수행할 수 있습니다.
# author는 작성자를 의미합니다. login의 users 모델을 참조합니다.
class Post(models.Model):
    author = models.ForeignKey(user_model.users, null=True, on_delete=models.CASCADE, related_name='post_author')
    image = models.ImageField(blank=False)
    caption = models.TextField(blank=False)
    image_likes = models.ManyToManyField(user_model.users, blank=True, related_name='post_image_likes')

    def __str__(self):
        return f"{self.author}:{self.caption}"

class Comment(models.Model):
    author = models.ForeignKey(user_model.users, null=True, on_delete=models.CASCADE, related_name='comment_author')
    posts = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, related_name='comment_post')
    contents = models.TextField(blank=True)

    def __str__(self):
        return f"{self.author}:{self.contents}"