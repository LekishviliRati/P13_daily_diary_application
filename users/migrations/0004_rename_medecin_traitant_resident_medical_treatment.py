# Generated by Django 4.0.1 on 2022-01-31 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_medical_treatment_resident_medecin_traitant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resident',
            old_name='medecin_traitant',
            new_name='medical_treatment',
        ),
    ]
