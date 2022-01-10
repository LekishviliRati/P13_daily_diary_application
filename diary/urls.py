from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='diary-home'),
    path('post/', views.post, name='diary-post'),
    path('about/', views.about, name='diary-about'),

]