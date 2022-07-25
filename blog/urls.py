from django.contrib import admin
from django.urls import path
# from blog import views
from .views import BlogView, BlogDetail

urlpatterns = [
    # path('',views.blog,name="Blog"),
    path ('', BlogView.as_view(), name = "Blog"),
    path("<int:pk>", BlogDetail.as_view(), name="BlogDetail"),
]