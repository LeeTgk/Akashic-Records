from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.utils.translation import gettext_lazy as _
from .models import Post
from .forms import PostForm

@login_required
def list_posts(request):

    if request.user.is_superuser:
        posts = Post.objects.filter()
    else:
        posts = Post.objects.filter(created_by=request.user)

    context = {
        'posts': posts
    }
    
    return render(request, 'posts/list.html', context=context)

@login_required
def edit_post(request, post_id):

    post = get_object_or_404(Post, post_id=post_id)

    if not ((post.created_by == request.user) or (request.user.is_superuser)):
        messages.add_message(request, messages.ERROR, _('Você não pode editar este post!\n'))
        return redirect(reverse('list_posts'))

    if request.method == 'POST':
        formPost = PostForm(request.POST, instance=post)
        if formPost.is_valid():
            post = formPost.save()
            post.save()

            messages.add_message(request, messages.INFO, _('Salvo com sucesso!\n'))

            return redirect(reverse('list_posts'))

    formPost = PostForm(instance=post)

    context = {
        'form': formPost
    }

    return render(request, 'posts/edit.html', context=context)

@login_required
def delete_post(request, post_id):

    post = get_object_or_404(Post, post_id=post_id)

    if not ((post.created_by == request.user) or (request.user.is_superuser)):
        messages.add_message(request, messages.ERROR, _('Você não pode editar este post!\n'))
        return redirect(reverse('list_posts'))

    post.delete()
    messages.add_message(request, messages.INFO, _('Deletado com sucesso!\n'))

    return redirect(reverse('list_posts'))


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