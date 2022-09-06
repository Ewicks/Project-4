from . import views
from django.urls import path
from .views import PostList, ArticleDetailView

urlpatterns = [
    path("blog/", PostList.as_view(), name="blog"),
    path("blog/", views.blog, name="blog"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("index/", views.index, name="index"),
    path("article/<int:pk>", ArticleDetailView.as_view(), name="article-detail"),

]