from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="index"),
    path("blog/", views.blog, name="blog"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]