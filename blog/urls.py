from . import views
from django.urls import path
from .views import PostList, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path("blog/", PostList.as_view(), name="blog"),
    path("blog/", views.blog, name="blog"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("", views.index, name="index"),
    path("article/<int:pk>", ArticleDetailView.as_view(), name="article-detail"),
    path("add_post/", AddPostView.as_view(), name="add_post"),
    path("article/edit/<int:pk>", UpdatePostView.as_view(), name="update_post"),
    path("article/<int:pk>/delete", DeletePostView.as_view(), name="delete_post"),
]

