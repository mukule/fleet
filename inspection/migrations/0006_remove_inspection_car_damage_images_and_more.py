# Generated by Django 4.2.3 on 2023-12-28 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0005_remove_inspection_drivers_signature_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inspection',
            name='car_damage_images',
        ),
        migrations.AddField(
            model_name='inspection',
            name='car_damage_images',
            field=models.ImageField(blank=True, null=True, upload_to='car_damage_images/'),
        ),
    ]
