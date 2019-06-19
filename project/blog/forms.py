from django import forms
from django.db import models

from .models import Post


class CreatePostForm(forms.ModelForm):
    text = forms.CharField()
    title = forms.CharField()

    class Meta:
        model = Post
        fields = ('text', 'title')



