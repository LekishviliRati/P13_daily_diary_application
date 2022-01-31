from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 350 or img.width > 350:
            output_size = (350, 350)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Resident(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    birth_date = models.DateField()
    place_of_birth = models.CharField(max_length=50)
    relatives = models.TextField()
    secret_information = models.TextField()
    surgeries = models.TextField()
    treating_doctor = models.CharField(max_length=250)
    medical_treatment = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} '

