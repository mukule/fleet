# Generated by Django 4.2.3 on 2023-08-11 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0026_remove_inspectionitemstatus_damages_noted_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carinspection',
            name='damages_noted',
        ),
        migrations.RemoveField(
            model_name='carinspection',
            name='fuel_in',
        ),
        migrations.RemoveField(
            model_name='carinspection',
            name='fuel_out',
        ),
        migrations.RemoveField(
            model_name='carinspection',
            name='kms_allowed',
        ),
        migrations.RemoveField(
            model_name='carinspection',
            name='kms_driven',
        ),
        migrations.RemoveField(
            model_name='carinspection',
            name='kms_in',
        ),
        migrations.RemoveField(
            model_name='carinspection',
            name='kms_out',
        ),
    ]
