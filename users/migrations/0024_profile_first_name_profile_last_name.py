# Generated by Django 4.0.1 on 2022-02-12 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_alter_profile_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='null', max_length=150),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='null', max_length=150),
        ),
    ]