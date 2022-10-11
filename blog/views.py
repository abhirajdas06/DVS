from re import template
from unicodedata import category
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from blog.models import Post, Category, Comment

# Create your views here.
# def blog(request):
#     #  return HttpResponse("Hello Home")
#     return render(request, "blog.html")

class BlogView(ListView):
    model = Post
    template_name = "blog.html"
    ordering = ['-date']

class BlogDetail(DetailView):
    model = Post
    template_name = "blog_details.html"
    # comment = Comment.objects.filter(post=post)
# def CategoryView(request,cats):
#     return render(request, 'category.html',{'cats':cats}),    

def category(request, slug):
    category = Category.objects.get (slug=slug)
    
    context = {
        'category' : category
    }
    
    return render (request, 'category.html', context)

def postComment(request):
        if request.method =='POST':
            name = request.POST['name']
            email = request.POST['email']
            body = request.POST['body']
            postId =request.POST.get('postId')
            post= Post.objects.get(id=postId)
            comment=Comment(body= body, name=name, post=post, email=email)
            comment.save()
            
        return redirect(f"/blog/{post.slug}")
