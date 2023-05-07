from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
def home_view(request):
    blog_post = Post.objects.all()[:4]
    context = {'blog_post': blog_post}
    return render(request, 'blog/index.html', context=context )


def single_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {'post':post}
    return render(request, 'blog/single.html', context=context )