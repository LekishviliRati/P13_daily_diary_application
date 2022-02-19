from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image


class Resident(models.Model):
    last_name = models.CharField(max_length=40)
    first_name = models.CharField(max_length=40)
    birth_date = models.DateField()
    place_of_birth = models.CharField(max_length=50)
    secret_information = models.TextField()
    surgeries = models.TextField()
    relatives = models.TextField(default='Pas de proches')
    treating_doctor = models.CharField(max_length=250)
    medical_treatment = models.TextField()
    entry_date = models.DateField(default=timezone.now)
    image = models.ImageField(default='default.jpg', upload_to='pics')
    floor = models.CharField(max_length=20, default='1')
    room_number = models.CharField(max_length=20, default='1')
    material = models.TextField(default='Pas de matériels')
    activities = models.TextField(default='Pas inscrit aux activités')

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name} '

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 350 or img.width > 350:
            output_size = (350, 350)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='pics')
    phone_number = models.CharField(default='Pas renseigné', max_length=40)
    address = models.CharField(default='Pas renseigné', max_length=150)
    status = models.CharField(default='2', max_length=20, choices=(('1', 'employee'), ('2', 'relative')))
    relatives = models.ManyToManyField(Resident)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 350 or img.width > 350:
            output_size = (350, 350)
            img.thumbnail(output_size)
            img.save(self.image.path)
