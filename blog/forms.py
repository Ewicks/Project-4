from django import forms
from .models import Comment, Post, Contact


class CommentForm(forms.ModelForm):
    """
    Field to be displayed in the CommentForm
    """
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    """
    Fields to be displayed in the PostForm
    """
    class Meta:
        model = Post
        fields = (
            'title', 'slug', 'content', 'featured_image', 'status', 'topics',)


class ContactForm(forms.ModelForm):
    """
    All fields from the Contact model will be displayed in the ContactForm
    """
    class Meta:
        model = Contact
        fields = "__all__"
