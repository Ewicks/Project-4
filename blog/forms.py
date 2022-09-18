from django import forms
from .models import Comment, Post, Contact


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title', 'slug', 'content', 'featured_image', 'status', 'topics',)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"