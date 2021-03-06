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
# def post(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'diary/posts.html', context)
#

# class based view
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'diary/posts.html'
    context_object_name = 'posts'  # Without context_object_name nos posts are displayed
    ordering = ['-date']  # Display Posts from earliest to oldest
    paginate_by = 5


class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'diary/user_posts.html'
    context_object_name = 'posts'  # Without context_object_name nos posts are displayed
    ordering = ['-date']  # Display Posts from earliest to oldest
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'resident', 'content']

    # Initialise resident value
    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(**kwargs)
        initial['resident'] = self.kwargs.get('pk')  # Get pk in url to initialise resident field.
        return initial

    def form_valid(self, form):
        form.instance.author = self.request.user  # To publish a post, need author id.
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # To publish a post need to specify author id
        return super().form_valid(form)

    # User asking for updating post must be the author of the post
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


# new residents posts list view
class ResidentPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'diary/resident_posts.html'
    context_object_name = 'posts'  # Without context_object_name nos posts are displayed
    ordering = ['-date']  # Display Posts from earliest to oldest
    paginate_by = 5

    def get_queryset(self):
        resident_id = self.kwargs.get('id')
        post = Post.objects.filter(resident=resident_id)
        return post

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        user = get_object_or_404(User, username=self.request.user.username)
        context['user_relatives_list'] = user.profile.relatives.all()
        return context


# New not found handler
def handler404(request, exception):
    return render(request, 'users/404.html')
