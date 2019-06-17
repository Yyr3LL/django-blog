from django.shortcuts import render
from .models import Post


def main_page(request):
	l = Post.objects.all()
	return render(request, 'index.html', {'list': l})

def post_list(request):
    p = Post.objects.all()
    return render(request, 'posts.html', {'post': p})
