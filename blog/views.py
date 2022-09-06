from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog.html"
    paginate_by = 6


class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"


def about(request):
    """ A view to return the about page """
    return render(request, 'about.html')

def contact(request):
    """ A view to return the contact page """
    return render(request, 'contact.html')

def blog(request):
    """ A view to return the blog page """
    return render(request, 'blog.html')

def index(request):
    """ A view to return the blog page """
    return render(request, 'index.html')


