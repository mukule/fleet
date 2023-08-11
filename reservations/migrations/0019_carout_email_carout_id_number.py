# Generated by Django 4.2.3 on 2023-08-11 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0018_alter_carout_number_plate'),
    ]

    operations = [
        migrations.AddField(
            model_name='carout',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='carout',
            name='id_number',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]