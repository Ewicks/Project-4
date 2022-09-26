from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, View)
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages

from .models import Post
from .forms import CommentForm, PostForm, ContactForm


def TopicView(request, tops):
    topics_posts = Post.objects.filter(topics=tops)
    return render(request, 'topics.html', {
        'tops': tops, 'topics_posts': topics_posts})


class PostDetail(View):
    def get(self, request, pk, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, id=pk)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        template = "article_details.html"
        context = {
            "post": post,
            "comments": comments,
            "commented": False,
            "comment_form": CommentForm()
        }
        return render(request, template, context)

    def post(self, request, pk, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, id=pk)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "article_details.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
            },
        )


class PostLike(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.info(request, 'unliked')
        else:
            messages.success(request, 'liked')
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('article-detail', args=[post.id]))


class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog.html"
    paginate_by = 6
    ordering = ["-updated_on"]


@login_required
def add_post(request):
    post_form = PostForm(request.POST or None, request.FILES)
    if request.method == "POST":
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            messages.success(request, 'post added')
            return redirect("blog")
    template = "add_post.html"
    context = {
        "form": post_form,
    }
    return render(request, template, context)


@login_required
def update_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    user = get_object_or_404(User, username=request.user)
    if post.author != user:
        messages.error(request, 'Access denied')
        return redirect(reverse('blog'))
    post_form = PostForm(instance=post)

    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, instance=post)
        if post_form.is_valid():
            post_form.save()
            messages.success(request, 'post updated')
            return redirect("blog")
    template = "update_post.html"
    context = {
        'post': post,
        'form': post_form,
    }
    return render(request, template, context)


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('blog')


@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    user = get_object_or_404(User, username=request.user)
    if post.author != user:
        messages.error(request, 'Access denied')
        return redirect(reverse('blog'))
    post.delete()
    messages.info(request, 'post deleted')
    return redirect(reverse('blog'))


def about(request):
    """ A view to return the about page """
    return render(request, 'about.html')


def index(request):
    """ A view to return the blog page """
    return render(request, 'index.html')


def contact(request):
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for your message')
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def search_posts(request):
    if request.method == "POST":
        searched = request.POST['searched']
        posts = Post.objects.filter(
            Q(title__icontains=searched) |
            Q(featured_image__icontains=searched) |
            Q(author__username__icontains=searched) |
            Q(content__icontains=searched) |
            Q(created_on__icontains=searched) |
            Q(likes__username__icontains=searched))
        messages.info(request, f"{request.POST['searched']} results")

        return render(
            request, 'search_posts.html',
            {'searched': searched, 'posts': posts})
    else:
        return render(request, 'search_posts.html',  {})
