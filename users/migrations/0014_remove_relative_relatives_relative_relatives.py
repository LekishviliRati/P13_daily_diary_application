# Generated by Django 4.0.1 on 2022-02-07 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_remove_resident_relatives_relative_relatives'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relative',
            name='relatives',
        ),
        migrations.AddField(
            model_name='relative',
            name='relatives',
            field=models.ManyToManyField(to='users.Resident'),
        ),
    ]
