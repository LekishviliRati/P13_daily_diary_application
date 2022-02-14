from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    ResidentPostListView
)

urlpatterns = [
    path('', views.home, name='diary-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('resident_post/<int:id>', ResidentPostListView.as_view(), name='resident-posts'),
    # Function based view  : path('post/', views.post, name='diary-post'),
    # Class based view : path('post/', PostListView.as_view(), name='diary-post'),
    path('post/', PostListView.as_view(), name='diary-post'),
    path('post/article/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/article/<int:pk>/new/', PostCreateView.as_view(), name='post-create'),
    path('post/article/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/article/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='diary-about'),
]