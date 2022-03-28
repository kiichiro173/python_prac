# 投稿フォームの追加！！
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        # データベースに関して
        model = Comment
        fields = ["name", "email", "body"]