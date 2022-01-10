from django.shortcuts import render
from . models import Post


def home(request):
    return render(request, 'diary/home.html')


def post(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'diary/posts.html', context)


def about(request):
    return render(request, 'diary/about.html', {'title': 'About'})
