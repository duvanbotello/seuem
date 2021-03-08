from django import forms

from ckeditor.fields import RichTextField

from article.models import Post


class PostForm(forms.ModelForm):
    userName = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    title = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    content = RichTextField()

    class Meta:
        model = Post
        fields = ('userName', 'title', 'content',)
