# Generated by Django 4.0.1 on 2022-02-13 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_alter_profile_address_alter_profile_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('1112', 'employee'), ('25727', 'relative')], default='1', max_length=20),
        ),
    ]