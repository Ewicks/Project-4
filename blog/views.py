from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        # comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog.html",
            {
                "post": post,
                # "comments": comments,
                "commented": False,
                "liked": liked,
                # "comment_form": CommentForm()
            },
        )

def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        # comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # comment_form = CommentForm(data=request.POST)
        # if comment_form.is_valid():
        #     comment_form.instance.email = request.user.email
        #     comment_form.instance.name = request.user.username
        #     comment = comment_form.save(commit=False)
        #     comment.post = post
        #     comment.save()
        # else:
        #     comment_form = CommentForm()

        return render(
            request,
            "blog.html",
            {
                "post": post,
                # "comments": comments,
                # "commented": True,
                # "comment_form": comment_form,
                "liked": liked
            },
        )

class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('article_details', args=[slug]))

class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog.html"
    paginate_by = 6
    ordering = ["updated_on"]
    # ordering = ["-id"]


class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"


class AddPostView(CreateView):
    model = Post
    # form_class = PostForm
    template_name = "add_post.html"
    fields = "__all__"
    # field = ('title', 'content')


class UpdatePostView(UpdateView):
    model = Post
    template_name = "update_post.html"
    fields = ['title', 'content']


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('blog')

def about(request):
    """ A view to return the about page """
    return render(request, 'about.html')

def contact(request):
    """ A view to return the contact page """
    return render(request, 'contact.html')

def index(request):
    """ A view to return the blog page """
    return render(request, 'index.html')


