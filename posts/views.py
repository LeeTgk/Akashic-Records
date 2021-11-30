from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from .models import Post

@login_required
def show_posts(request):
    posts = Post.objects.filter(created_by=request.user)

    context = {
        'posts': posts
    }

    return render(request, '', context=context)