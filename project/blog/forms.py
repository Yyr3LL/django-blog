from django import forms
from django.db import models

from .models import Post


class CreatePostForm(forms.ModelForm):
    # author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = forms.CharField()
    text = forms.CharField()

    class Meta:
        model = Post
        fields = ('title', 'text')



