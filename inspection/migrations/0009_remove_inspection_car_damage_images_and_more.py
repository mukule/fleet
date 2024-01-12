# Generated by Django 4.2.3 on 2024-01-12 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0008_remove_inspection_car_damage_images_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inspection',
            name='car_damage_images',
        ),
        migrations.AddField(
            model_name='inspection',
            name='car_damage_images',
            field=models.ManyToManyField(blank=True, related_name='inspections_damage_images', to='inspection.damageimage'),
        ),
    ]
