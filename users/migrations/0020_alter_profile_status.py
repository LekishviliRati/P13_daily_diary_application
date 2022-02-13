# Generated by Django 4.0.1 on 2022-02-12 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_alter_profile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('employee', 1), ('relative', 2)], default='1', max_length=20),
        ),
    ]
