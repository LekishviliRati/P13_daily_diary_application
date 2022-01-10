from django.shortcuts import render

posts = [
    {
        'author': 'Rati',
        'title': 'Post 1',
        'content': 'First pos content',
        'date': '9 Janvier 2022'
    },
    {
        'author': 'Ratii',
        'title': 'Post 2',
        'content': 'Second post content',
        'date': '10 Janvier 2022'
    }
]


def home(request):
    return render(request, 'diary/home.html')


def post(request):
    context = {
        'posts': posts
    }
    return render(request, 'diary/posts.html', context)


def about(request):
    return render(request, 'diary/about.html', {'title': 'About'})
