from django.db import models
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField("title", max_length=120)
    generated_text = models.TextField("generated_text")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="created_by", on_delete=models.CASCADE)
    created_at = models.DateTimeField("created_at", auto_now_add=True)
    updated_at = models.DateTimeField("updated_at", auto_now=True)

# Create your models here.
