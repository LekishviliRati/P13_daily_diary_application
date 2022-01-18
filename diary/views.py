from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):
    return render(request, 'diary/home.html')


# function based view
def post(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'diary/posts.html', context)


# class based view
class PostListView(ListView):
    model = Post
    template_name = 'diary/posts.html'
    context_object_name = 'posts'  # Without context_object_name nos posts are displayed
    ordering = ['-date']  # Display Posts from earliest to oldest
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'diary/user_posts.html'
    context_object_name = 'posts'  # Without context_object_name nos posts are displayed
    ordering = ['-date']  # Display Posts from earliest to oldest
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user    # To publish a post need to specify author id
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user    # To publish a post need to specify author id
        return super().form_valid(form)

    # User asking for updating article must be the author of it
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/post/'

    # User asking for updating article must be the author of it
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'diary/about.html', {'title': 'About'})
