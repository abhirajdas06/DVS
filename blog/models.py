import email
from turtle import title
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField
from django_extensions.db.fields import AutoSlugField
# from autoslug import AutoSlugField


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from=['title'])

    
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from=['title'])
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="blog/")
    meta_title = models.CharField(max_length=255)
    description = models.CharField(max_length=225)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE)
    # slug = models.SlugField(max_length=225, unique=True)
    
    # slug = AutoSlugField(populate_from=lambda instance: instance.title, slugify=lambda value: value.replace(' ','_'))
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)   
    name = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    email = models.EmailField()
    
    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)