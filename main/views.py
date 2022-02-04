from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from login import models as user_model # login의 모델에서 작성했던 users 모델을 사용할 겁니다.
from main import models as post_model
# Create your views here.


# 먼저, 회원 여부를 검증해야 하지만 제외함.
# 그러므로, 회원 여부에 관계없이 post 전부 출력->1인용 인스타 그램
def Main_feed(request):
    if request.method == "GET":
        comment_form = CommentForm() # forms.py 에다가 정의 해야함...
        user = get_object_or_404(user_model, pk=request.users.id)
        posts = post_model.Post.objects.all().order_by("-create_at")

        serializer = serializers.PostSerializer(posts,many=True)

        return render(request,'main/main.html',{"posts":serializer.data, "comment_form":comment_form})

def post_create(request):
    if request.method == "GET":
        form = CreatePostForm()
        return render(request, 'main/main.html',{"form":form})
    elif request.method == "POST":
        user = get_object_or_404(user_model, pk=request.users.id)
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = user
            post.save()
        else:
            print(form.errors)
        return render(request, 'main/main.html')



