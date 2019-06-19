from django.shortcuts import render
from .forms import CreatePostForm
from .models import Post


def home(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            pass
        else:
            form = CreatePostForm()
    return render(request, "home.html", {'form': form})


def main_page(request):
    l = Post.objects.all()
    return render(request, 'index.html', {'list': l})


def post_list(request):
    p = Post.objects.all()
    return render(request, 'posts.html', {'post': p})
