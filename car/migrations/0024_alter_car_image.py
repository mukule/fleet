# Generated by Django 4.2.3 on 2023-09-29 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0023_alter_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, default='default_image.jpg', null=True, upload_to='car_images/'),
        ),
    ]
