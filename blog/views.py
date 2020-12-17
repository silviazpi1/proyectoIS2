from django.shortcuts import render, get_object_or_404
from .models import Post 

def home(request):
    context = {}
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, "index.html", context)

""" def about(request):
    return render(request, "about.html", {})

def post(request, slug):
    product = get_object_or_404(Post, slug=slug)
    context = {
        'post': post
    }
    return render(request, "post.html", context) """
