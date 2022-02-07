# Generated by Django 4.0.1 on 2022-02-07 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_remove_resident_relatives'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='relatives',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.relative'),
        ),
    ]
