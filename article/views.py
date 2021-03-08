from django.shortcuts import render
from django.views.generic.list import ListView
from .models import User, Post
from .forms import PostForm
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse('<a href=add_post/>Add Post</a>')


class AddPostView(ListView):
    model = Post

    def get(self, request):
        form = PostForm()
        return render(request, 'app1/index.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            userName = form.cleaned_data['userName']
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            user_obj = User.objects.get(user_name=userName)
            add_post = Post.objects.create(user=user_obj, title=title, content=content)
            add_post.save()
            form = PostForm()
            return render(request, 'app1/index.html', {'form': form})


class SeePostView(AddPostView):
    model = Post

    def get(self, request):
        all_post = self.model.objects.all().order_by('-id')
        return render(request, 'app1/all_post.html', {'posts': all_post})
