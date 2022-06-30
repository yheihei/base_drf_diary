from dataclasses import field, fields
from django.shortcuts import render

# Create your views here.
from .models import Post
from rest_framework import viewsets
from rest_framework import serializers

# Create your views here.
def index(request):
  return render(request, 'index.html', {
    'posts': Post.objects.all(),
  })


class PostSerializer(serializers.ModelSerializer):
  class  Meta:
    model = Post
    fields = "__all__"


class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  '''
  これだけで下記が全部できちゃう

  一覧取得 GET /api/posts/
  詳細取得 GET /api/posts/<id>/
  新規作成 POST /api/posts/
  更新     PUT /api/posts/<id>/
  削除     DELETE /api/posts/<id>/
  '''
