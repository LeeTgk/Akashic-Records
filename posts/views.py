from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from .models import Post
import requests
import uuid

@login_required
def show_posts(request):
    posts = Post.objects.filter(created_by=request.user)

    context = {
        'posts': posts
    }

    return render(request, '', context=context)


def post(request):
    if request.user.is_authenticated:
        username = request.user
        title = request.POST.get('title')
        generatortext = request.POST.get('generatorText')
        texcon = request.POST.get('textContent')
        idtext = Post.objects.count() + 1

        if request.is_ajax():
            print('Printing Post: ', request.POST)
            post = Post(post_id=idtext,title=title,generator_text=generatortext,generated_text=texcon,created_by=username)
            post.save()

    return