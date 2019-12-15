from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views.generic import FormView, ListView, TemplateView

from .forms import CreatePostForm
from .models import Post


class MakePostView(FormView):
    template_name = "create_post.html"
    form_class = CreatePostForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/post_list/')


class MainPageView(TemplateView):
    template_name = "index.html"


class PostListView(ListView):
    template_name = "posts.html"
    queryset = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    context_object_name = "posts"
