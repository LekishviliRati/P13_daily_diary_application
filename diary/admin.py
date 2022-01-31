from django.contrib import admin
from .models import Post

# Add to the application admin page Posts table
admin.site.register(Post)

