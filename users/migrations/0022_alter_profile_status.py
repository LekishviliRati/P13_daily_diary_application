# Generated by Django 4.0.1 on 2022-02-12 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_alter_profile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[(1, 'employee'), (2, 'relative')], default='1', max_length=20),
        ),
    ]
