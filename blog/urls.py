from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="index"),
    path("blog/", views.PostList.as_view(), name="blog"),
    path("about/", views.PostList.as_view(), name="about"),
    path("contact/", views.PostList.as_view(), name="contact"),
    ]