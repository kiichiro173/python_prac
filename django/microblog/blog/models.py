import email
from statistics import mode
from turtle import title
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255) #文字の格納に関して
    slug = models.SlugField() # 投稿番号
    intro = models.TextField() # テキスト
    body = models.TextField() # 本文
    posted_date = models.DateTimeField(auto_now_add=True) # 投稿日時

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments",on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField() # 本文
    posted_date = models.DateTimeField(auto_now_add=True) # 投稿日時