from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponsePermanentRedirect

from django.utils import timezone


from .forms import CreatePostForm
from .models import Post
import random


def make_post(request):
    form = CreatePostForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/post_list/")
        else:
            form = CreatePostForm()
    return render(request, 'home.html', {'form': form})


def main_page(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'index.html', {'post': posts})


def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'posts.html', {'post': posts})
