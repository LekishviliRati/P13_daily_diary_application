# Generated by Django 4.0.1 on 2022-02-07 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_resident_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['user']},
        ),
        migrations.AlterModelOptions(
            name='resident',
            options={'ordering': ['last_name']},
        ),
        migrations.CreateModel(
            name='Relative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=40)),
                ('first_name', models.CharField(max_length=40)),
                ('phone_number', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=150)),
                ('residents', models.ManyToManyField(to='users.Resident')),
            ],
            options={
                'ordering': ['last_name'],
            },
        ),
    ]
