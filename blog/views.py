from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6

def about(request):
    """ A view to return the about page """
    return render(request, 'about.html')

def contact(request):
    """ A view to return the contact page """
    return render(request, 'contact.html')

def blog(request):
    """ A view to return the blog page """
    return render(request, 'blog.html')