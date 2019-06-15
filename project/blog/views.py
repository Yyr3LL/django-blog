from django.shortcuts import render
from .models import Post


def post_list(request):
    p = Post.objects.all()
    return render(request, 'index.html', {'post': p})
