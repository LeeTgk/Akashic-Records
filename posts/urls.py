from django import shortcuts
from django.urls import path

from .views import list_posts, edit_post, delete_post

urlpatterns = [
    path('', list_posts, name='list_posts'),
    path('edit/<int:post_id>', edit_post, name='edit_post'),
    path('delete/<int:post_id>', delete_post, name='delete_post')
]
