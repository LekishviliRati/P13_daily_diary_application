from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Resident


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)

    # __str__ method returns defined value instead of "obj 96xaUb..."
    def __str__(self):
        return self.title

    # To get to one post page, taking as argument primary key
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
