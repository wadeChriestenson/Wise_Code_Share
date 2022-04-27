from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post


# Create your views here.
def PostListView(request):
    post = Post.objects.all()
    print(post.values())
    return render(request, 'index.html', {'posts': post})
