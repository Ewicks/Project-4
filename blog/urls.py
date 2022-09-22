from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostList.as_view(), name="blog"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("index/", views.index, name="index"),
    path(
        "article/<int:pk>", views.PostDetail.as_view(), name="article-detail"),
    path("add_post/", views.add_post, name="add_post"),
    path("article/edit/<int:pk>", views.update_post, name="update_post"),
    path(
        "article/<int:pk>/delete", views.DeletePostView.as_view(), name="delete_post"),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('topic/<str:tops>/', views.TopicView, name='topic'),
    path('search_posts', views.search_posts, name='search_posts'),
]
