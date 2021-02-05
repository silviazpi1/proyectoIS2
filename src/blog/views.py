from django.shortcuts import render, get_object_or_404
from .models import Post 

def home(request):
    context = {}
    nombre = request.GET.get("nombre")
    tag = request.GET.get("tag")

    if nombre:
        posts = Post.objects.filter(nombre=nombre)
    elif tag:
        posts = Post.objects.filter(tag = tag)
    else:
        posts = Post.objects.all().order_by('-time')

    context = {
        'posts': posts
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html", {})

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post
    }
    print(post)
    return render(request, "post.html", context)
