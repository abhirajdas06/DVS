from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from blog.models import Post

# Create your views here.
# def blog(request):
#     #  return HttpResponse("Hello Home")
#     return render(request, "blog.html")

class BlogView(ListView):
    model = Post
    template_name = "blog.html"

class BlogDetail(DetailView):
    model = Post
    template_name = "blog_details.html"