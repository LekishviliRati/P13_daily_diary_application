# Generated by Django 4.0.1 on 2022-02-13 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_alter_profile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('1112', 'employee'), ('25727', 'relative')], default='2', max_length=20),
        ),
    ]
