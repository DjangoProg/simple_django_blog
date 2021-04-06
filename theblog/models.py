from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=250)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f'{self.title} - {self.author}'

    def get_absolute_url(self):
        # return reverse('post-detail', args=[str(self.pk)] )
        return reverse('home')


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return str(self.author)
