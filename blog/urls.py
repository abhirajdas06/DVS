from django.contrib import admin
from django.urls import path
from blog import views
from .views import BlogView, BlogDetail, category

urlpatterns = [
    # path('',views.blog,name="Blog"),
    path('postComment', views.postComment, name="PostComment"),
    path ('', BlogView.as_view(), name = "Blog"),
    path("<slug:slug>", BlogDetail.as_view(), name="BlogDetail"),
    path('category/<slug:slug>', category, name='Category'),
]